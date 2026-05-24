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

@st.cache_data(show_spinner="Baixando e processando dados oficiais do TSE...")
def get_tse_data():
    """
    Função para baixar e processar os dados do TSE para MS 2024.
    Cruza dados de candidatos com resultados de votação.
    """
    try:
        # URLs dos dados de 2024
        url_cand = "https://cdn.tse.jus.br/estatistica/sead/odsele/consulta_cand/consulta_cand_2024.zip"
        url_vote = "https://cdn.tse.jus.br/estatistica/sead/odsele/votacao_candidato_munzona/votacao_candidato_munzona_2024.zip"

        def download_and_extract_ms(url, filename_pattern):
            r = requests.get(url)
            with zipfile.ZipFile(io.BytesIO(r.content)) as z:
                # Localiza o arquivo de MS dentro do ZIP
                ms_file = [f for f in z.namelist() if filename_pattern in f][0]
                with z.open(ms_file) as f:
                    return pd.read_csv(f, sep=';', encoding='latin-1')

        # 1. Dados de Candidatos (para nomes, partidos, cargos)
        df_cand = download_and_extract_ms(url_cand, "consulta_cand_2024_MS.csv")
        # Filtrar apenas vereadores
        df_cand = df_cand[df_cand['DS_CARGO'] == 'VEREADOR']
        
        # 2. Dados de Votação (para votos e situação)
        df_vote = download_and_extract_ms(url_vote, "votacao_candidato_munzona_2024_MS.csv")
        
        # Mapeamento flexível de colunas (o TSE às vezes muda o nome entre DS_SITUACAO_TOT_TURNO e DS_SITUACAO_CANDIDATO_TOT)
        col_situacao = 'DS_SITUACAO_TOT_TURNO'
        if col_situacao not in df_vote.columns:
            if 'DS_SITUACAO_CANDIDATO_TOT' in df_vote.columns:
                col_situacao = 'DS_SITUACAO_CANDIDATO_TOT'
            else:
                # Se não encontrar nenhuma, tenta listar as disponíveis para diagnóstico
                raise KeyError(f"Coluna de situação não encontrada. Disponíveis: {list(df_vote.columns)[:10]}...")

        # Agrupar votos por candidato
        df_vote_grouped = df_vote.groupby('SQ_CANDIDATO').agg({
            'QT_VOTOS_NOMINAIS': 'sum',
            col_situacao: 'first'
        }).reset_index()
        
        # Padroniza o nome da coluna de situação para o resto do app
        df_vote_grouped = df_vote_grouped.rename(columns={col_situacao: 'DS_SITUACAO_TOT_TURNO'})

        # 3. Cruzamento (Merge)
        cols_cand = ['SQ_CANDIDATO', 'NM_URNA_CANDIDATO', 'SG_PARTIDO', 'NM_MUNICIPIO', 'NR_CANDIDATO']
        df_final = pd.merge(df_cand[cols_cand], df_vote_grouped, on='SQ_CANDIDATO', how='inner')
        
        # Se o merge resultar vazio, tenta um merge menos restritivo ou avisa
        if df_final.empty:
            raise ValueError("O cruzamento de dados (merge) resultou em uma tabela vazia.")
        
        return df_final
    
    except Exception as e:
        # Em caso de erro (ex: link fora do ar), gera dados simulados para demonstração
        st.error(f"Erro ao acessar dados reais do TSE: {e}. Exibindo dados de demonstração.")
        data = {
            'NM_MUNICIPIO': ['CAMPO GRANDE', 'CAMPO GRANDE', 'DOURADOS', 'TRÊS LAGOAS', 'CORUMBÁ'],
            'NM_URNA_CANDIDATO': ['JOÃO DO POVO', 'MARIA DA SAÚDE', 'ZÉ DA VILA', 'ANA DA EDUCAÇÃO', 'CARLOS DO MS'],
            'SG_PARTIDO': ['PL', 'PT', 'PSDB', 'MDB', 'PP'],
            'NR_CANDIDATO': [22123, 13456, 45789, 15000, 11222],
            'QT_VOTOS_NOMINAIS': [5432, 4890, 3210, 2100, 1800],
            'DS_SITUACAO_TOT_TURNO': ['ELEITO', 'ELEITO', 'SUPLENTE', 'ELEITO', 'SUPLENTE']
        }
        return pd.DataFrame(data)

# Título e Header
st.title("🏛️ Sistema de Consulta Eleitoral MS 2024")
st.subheader("Relatório Interativo de Vereadores e Suplentes")

# Sidebar - Filtros
st.sidebar.image("https://www.tse.jus.br/imagens/logos/tse-logo.png", width=150)
st.sidebar.header("🔍 Painel de Busca")

# Carregamento dos dados
df = get_tse_data()

# Filtros Dinâmicos
cidades = sorted(df['NM_MUNICIPIO'].unique())
cidade_sel = st.sidebar.selectbox("Escolha a Cidade", cidades)

partidos = sorted(df['SG_PARTIDO'].unique())
partido_sel = st.sidebar.multiselect("Filtrar por Partido", partidos)

situacoes = sorted(df['DS_SITUACAO_TOT_TURNO'].unique())
situacao_sel = st.sidebar.multiselect("Situação Final", situacoes, default=situacoes)

# Lógica de Filtragem
df_filtered = df[df['NM_MUNICIPIO'] == cidade_sel]

if partido_sel:
    df_filtered = df_filtered[df_filtered['SG_PARTIDO'].isin(partido_sel)]

if situacao_sel:
    df_filtered = df_filtered[df_filtered['DS_SITUACAO_TOT_TURNO'].isin(situacao_sel)]

# Área Principal - Métricas
m1, m2, m3 = st.columns(3)
with m1:
    st.metric("Total de Candidatos", len(df_filtered))
with m2:
    votos_totais = df_filtered['QT_VOTOS_NOMINAIS'].sum()
    st.metric("Votos Apurados (Filtro)", f"{votos_totais:,}".replace(",", "."))
with m3:
    eleitos = len(df_filtered[df_filtered['DS_SITUACAO_TOT_TURNO'].str.contains('ELEITO', na=False)])
    st.metric("Eleitos Listados", eleitos)

# Tabela de Resultados
st.markdown("---")
st.write(f"### Lista de Candidatos em {cidade_sel}")

# Renomeando colunas para o usuário
df_display = df_filtered[['NM_URNA_CANDIDATO', 'NR_CANDIDATO', 'SG_PARTIDO', 'QT_VOTOS_NOMINAIS', 'DS_SITUACAO_TOT_TURNO']].copy()
df_display.columns = ['Nome na Urna', 'Número', 'Partido', 'Votos', 'Situação Final']

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
