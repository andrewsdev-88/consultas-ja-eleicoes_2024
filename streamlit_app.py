import streamlit as st
import pandas as pd
import requests
import zipfile
import io
import os

# Configuração da página
st.set_page_config(page_title="Relatório MS 2024 - Gabinett Style", layout="wide", page_icon="🗳️")

# Estilização CSS para um visual mais profissional (estilo dashboard)
st.markdown("""
    <style>
    .main {
        background-color: #f5f7f9;
    }
    .stMetric {
        background-color: #ffffff;
        padding: 15px;
        border-radius: 10px;
        box-shadow: 0 2px 4px rgba(0,0,0,0.05);
    }
    </style>
    """, unsafe_allow_html=True)

@st.cache_data(show_spinner="Realizando Auditoria e Carregamento de Dados Oficiais...")
def get_tse_data():
    try:
        # URLs Oficiais 2024 - Fontes de Verdade
        url_cand = "https://cdn.tse.jus.br/estatistica/sead/odsele/consulta_cand/consulta_cand_2024.zip"
        url_vote = "https://cdn.tse.jus.br/estatistica/sead/odsele/votacao_candidato_munzona/votacao_candidato_munzona_2024.zip"

        def download_and_extract_ms(url, filename_pattern):
            r = requests.get(url, timeout=30)
            with zipfile.ZipFile(io.BytesIO(r.content)) as z:
                ms_file = [f for f in z.namelist() if filename_pattern in f][0]
                with z.open(ms_file) as f:
                    return pd.read_csv(f, sep=';', encoding='latin-1', low_memory=False)

        # 1. VARREDURA DE CANDIDATOS
        df_cand = download_and_extract_ms(url_cand, "consulta_cand_2024_MS.csv")
        # Filtrar apenas vereadores com registros ativos
        df_cand = df_cand[df_cand['DS_CARGO'] == 'VEREADOR']
        
        # 2. VARREDURA DE VOTAÇÃO
        df_vote = download_and_extract_ms(url_vote, "votacao_candidato_munzona_2024_MS.csv")
        
        # Auditoria de Colunas de Situação (Mapeamento Exaustivo)
        # O log de erro mostrou que o nome correto é 'DS_SIT_TOT_TURNO'
        possiveis_colunas = ['DS_SIT_TOT_TURNO', 'DS_SITUACAO_TOT_TURNO', 'DS_SITUACAO_CANDIDATO_TOT', 'DS_SITUACAO_POS_PLEITO']
        col_situacao = next((c for c in possiveis_colunas if c in df_vote.columns), None)
        
        if not col_situacao:
            raise KeyError(f"Falha Crítica de Auditoria: Coluna de Situação não encontrada em {df_vote.columns}")

        # Agrupamento Seguro: Garante que votos de todas as zonas/seções sejam somados
        # SQ_CANDIDATO é a chave primária imutável do TSE
        df_vote_grouped = df_vote.groupby('SQ_CANDIDATO').agg({
            'QT_VOTOS_NOMINAIS': 'sum',
            col_situacao: 'first'
        }).reset_index()
        
        df_vote_grouped = df_vote_grouped.rename(columns={col_situacao: 'DS_SITUACAO_TOT_TURNO'})

        # 3. MERGE DE INTEGRIDADE TOTAL
        # Cruzamos por SQ_CANDIDATO (ID Interno) e validamos consistência
        df_final = pd.merge(
            df_cand[['SQ_CANDIDATO', 'NM_URNA_CANDIDATO', 'SG_PARTIDO', 'NM_MUNICIPIO', 'NR_CANDIDATO', 'DS_SITUACAO_CANDIDATURA']], 
            df_vote_grouped, 
            on='SQ_CANDIDATO', 
            how='left' # Usamos left para identificar se algum candidato ficou sem voto no registro
        )

        # Tratamento de Nulos (Candidatos com 0 votos ou não totalizados)
        df_final['QT_VOTOS_NOMINAIS'] = df_final['QT_VOTOS_NOMINAIS'].fillna(0).astype(int)
        df_final['DS_SITUACAO_TOT_TURNO'] = df_final['DS_SITUACAO_TOT_TURNO'].fillna('NÃO TOTALIZADO')
        
        return df_final
    
    except Exception as e:
        st.error(f"❌ FALHA NA AUDITORIA TÉCNICA: {e}")
        return pd.DataFrame()

# Título e Dashboard de Auditoria
st.title("🏛️ Auditoria Eleitoral MS 2024")
st.markdown("### Varredura Completa de Dados Públicos (TSE)")

# Carregamento com Auditoria
df = get_tse_data()

if df.empty:
    st.warning("⚠️ Atenção: A base de dados não pôde ser validada. Verifique a conexão com o servidor do TSE.")
    st.stop()

# Painel de Controle Lateral
st.sidebar.header("🛡️ Parâmetros de Filtro")
cidade_sel = st.sidebar.selectbox("Município", sorted(df['NM_MUNICIPIO'].unique()))

# Auditoria Local (Cidade Selecionada)
df_city = df[df['NM_MUNICIPIO'] == cidade_sel]

# Métricas de Auditoria
c1, c2, c3, c4 = st.columns(4)
with c1:
    st.metric("Total de Candidatos", len(df_city))
with c2:
    votos_val = df_city['QT_VOTOS_NOMINAIS'].sum()
    st.metric("Votação Total", f"{votos_val:,}".replace(",", "."))
with c3:
    eleitos = len(df_city[df_city['DS_SITUACAO_TOT_TURNO'].str.contains('ELEITO', na=False)])
    st.metric("Cadeiras (Eleitos)", eleitos)
with c4:
    partidos = df_city['SG_PARTIDO'].nunique()
    st.metric("Partidos na disputa", partidos)

# Filtro de Situação para o Usuário
st.sidebar.markdown("---")
situacoes = sorted(df_city['DS_SITUACAO_TOT_TURNO'].unique())
situacao_sel = st.sidebar.multiselect("Filtrar Situação Eleitoral", situacoes, default=situacoes)

df_filtered = df_city[df_city['DS_SITUACAO_TOT_TURNO'].isin(situacao_sel)]

# Tabela Auditada
st.write(f"#### Relatório Consolidado: {cidade_sel}")
df_display = df_filtered[['NM_URNA_CANDIDATO', 'NR_CANDIDATO', 'SG_PARTIDO', 'QT_VOTOS_NOMINAIS', 'DS_SITUACAO_TOT_TURNO']]
df_display.columns = ['Candidato', 'Número', 'Partido', 'Votos Totais', 'Situação Final']

st.dataframe(
    df_display.sort_values(by='Votos Totais', ascending=False),
    use_container_width=True,
    hide_index=True
)

st.dataframe(
    df_display.sort_values(by='Votos', ascending=False),
    use_container_width=True,
    hide_index=True
)

# Rodapé e Exportação
st.sidebar.markdown("---")
if st.sidebar.button("💾 Gerar Relatório CSV"):
    csv = df_display.to_csv(index=False).encode('utf-8')
    st.sidebar.download_button(
        label="Clique aqui para Baixar",
        data=csv,
        file_name=f'relatorio_eleitoral_{cidade_sel.lower().replace(" ", "_")}.csv',
        mime='text/csv',
    )

st.caption("Dados atualizados conforme base pública do TSE - Eleições Municipais 2024.")
