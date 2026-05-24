# **SYSTEM\_ARCHITECTURE.md — Framework de Fase Zero**

Line spacing: 1.25  
**Status:** Ativo / Lei Técnica e Visual Definitiva  
**Escopo:** Framework Universal para Desenvolvimento Acelerado por IA (Solo/Squads)  
**Versão:** 2026.2

## ---

**1\. Manifesto de Alinhamento e Filosofia Operacional**

Este documento é a **Lei Técnica e Visual Absoluta** para a concepção, desenvolvimento, auditoria e evolução de qualquer aplicação dentro deste ecossistema. Ele foi projetado para atuar como a **Memória Persistente Central** e o contexto de inicialização para Engenheiros de Software Humanos e Agentes de Inteligência Artificial. Nenhuma linha de código ou design deve ser alterada de forma a violar os princípios aqui estabelecidos.

### **1.1 Filosofia de Desenvolvimento (Vibe Coding Avançado)**

* **Clareza Estratégica Antes da Execução:** Entender o "porquê" precede o "como". Nenhuma linha de código deve ser escrita sem o devido mapeamento de dores e requisitos técnicos (PRD).  
* **Independência Técnica e Reuso:** Priorizar a construção de arquiteturas sólidas, escaláveis e componentizadas, reduzindo a dependência cega de plataformas no-code proprietárias quando o projeto exigir escala.  
* **Condução Centralizada, Execução Distribuída:** Os agentes aceleram a codificação e automação, mas a validação técnica, o direcionamento de produto e a tomada de decisões de arquitetura seguem rigorosamente as premissas deste documento.

## ---

**2\. Design System Robustificado & Tokenização Semântica**

A consistência visual é um processo automatizado e forçado via código. O design afasta-se de clichês tecnológicos genéricos e adota o padrão de **Brutalismo Refinado** e **Visual Cinematográfico Técnico**.

### **2.1 Interface Inventory (Prevenção de Retrabalho)**

Antes de qualquer refatoração ou criação de rotas, os agentes devem mapear o repositório para eliminar elementos redundantes. É proibido criar variações locais de botões, inputs ou cards. Se um elemento visual não estiver indexado nos átomos do projeto, ele deve ser componentizado ou rejeitado.

### **2.2 Atomic Design na Prática (shadcn/ui & Radix)**

O desenvolvimento de interfaces deve seguir rigorosamente a hierarquia atômica:

1. **Atoms (Componentes Core):** Localizados estritamente em components/ui (baseados em shadcn/ui e Radix UI primitives). Foco em acessibilidade (focus-visible, estados ARIA).  
2. **Molecules:** Junção de átomos (ex: um campo de busca composto por Input \+ Botão de Ícone).  
3. **Organisms:** Estruturas complexas e independentes (ex: Navbar, Formulário de Cadastro, Sidebar de Terminal). Utilizar CVA (*Class Variance Authority*) para gerenciar variantes de estilo de forma limpa.  
4. **Templates:** Estruturas de Grid e layouts de página (ex: Layout de Dashboard, Grid Brutalista).  
5. **Pages:** Instanciações dos templates alimentadas por dados e estados operacionais.

### **2.3 O Sistema de Tokens Sagrado (CSS-First & OKLCH)**

Se o projeto utilizar **Tailwind CSS v4**, a configuração de cores deve ser feita estritamente via variáveis de ambiente CSS nativas no bloco @theme, utilizando o modelo **OKLCH** para garantir uniformidade de percepção de contraste e acessibilidade automática.

#### **A Paleta Restrita Autorizada:**

* **Fundo Primário (bg-architectural-black):** Tons baseados em \#0A0A0A ou equivalente brutalista escuro. Sensação de "terminal no vazio".  
* **Texto Principal (text-warm-off-white):** Branco levemente aquecido (\#F7F7F7 ou similar) para mitigar a fadiga visual do contraste puro sobre o preto.  
* **Acento e Destaque (text-architectural-amber / bg-architectural-amber):** Tom âmbar dourado (\#D4A843), simbolizando luz de filamento técnico. Usado cirurgicamente em eyebrows, links ativos e CTAs principais.  
* **A Lista Negra Visual:** É **expressamente proibido** utilizar tons de verde Matrix vibrante (\#00FF41) ou ciano/teal (\#00B8A9). Desvios cromáticos quebram o posicionamento premium e corporativo do ecossistema.

### **2.4 Regras de Acabamento e Micro-Design**

* **Bordas e Cantos Brutalistas:** O valor máximo permitido de arredondamento de borda em qualquer elemento (botão, card, janela) é border-radius: 2px (rounded-sm). Ângulos retos e cantos secos dominam a estética.  
* **Gridlines Finas:** Divisores de seção devem usar linhas ultra-finas contínuas em tons de cinza ou âmbar escurecido (border-black-line). O grid estrutural deve guiar o olhar, eliminando sombras pesadas.  
* **A Regra Antidecapitação de Títulos:** Títulos em fontes Display condensadas e em caixa alta (uppercase), com line-height agressivo (1.02 a 1.05), tendem a sofrer cortes físicos em acentos maiúsculos (ex: "É", "Õ") se o container possuir overflow-hidden. Todo elemento h1, h2 ou h3 display deve possuir obrigatoriamente um padding-block de segurança de, no mínimo, 0.08em.  
* **Animações Atmosféricas:** Interações dinâmicas devem incluir janelas estilo *Blueprint Terminals* (fundo semitransparente com backdrop-blur e bg-black-soft/70), animações de escrita (*Typing*), cursores interativos piscantes (animate-blink), e chuva de código em canvas renderizada estritamente em tons de âmbar com opacidade reduzida entre 10% e 15%.  
* **Ritmo Editorial:** Alternar intencionalmente entre seções densas (especificações, tabelas) e seções de respiro (frase única de manifesto com espaço negativo ativo). Máximo de 2 parágrafos por coluna de manifesto.

## ---

**3\. Engenharia de Contratos & Sincronia Backend (SRP)**

No ambiente do servidor, os conceitos de componentização e tokenização são traduzidos para a disciplina de contratos rigorosos de software.

### **3.1 Alinhamento de Terminologia Técnica**

* **Atomização no Servidor:** Convertida no **Single Responsibility Principle (SRP)**. Módulos e funções executam apenas uma única unidade de responsabilidade de negócio.  
* **Componentização Lógica:** Traduzida no padrão de **Services e Providers** isolados e modulares.  
* **Tokenização de Dados:** Expressa na arquitetura de **Shared Schemas de Validação (Zod / TypeScript)** atuando como a fonte única da verdade (Single Source of Truth) entre o banco de dados e a interface.

### **3.2 A Arquitetura de Contratos Compartilhados (Shared End-to-End)**

Toda mutação ou transporte de dados deve ser governada por um contrato central que trafega de ponta a ponta na aplicação:

* **Sincronia Total:** Se um novo campo for adicionado ou alterado no Schema de validação, o compilador deve quebrar o build imediatamente tanto no Backend (reclamando da persistência) quanto no Frontend (reclamando do consumo do componente).  
* **Refatoração Segura:** A tipagem estrita via TypeScript e Schemas compartilhados deve permitir alterações e renomeações em segundos em todo o projeto (Fullstack) usando ferramentas nativas de Refatoração da IDE ("Rename Symbol") sem riscos de quebra de comunicação.  
* **Next.js Server Actions:** Em ambientes Next.js com App Router, a tipagem deve viajar diretamente do servidor para o cliente de maneira nativa, eliminando a necessidade de geradores de tipos externos redundantes.

## ---

**4\. Disciplina de Repositório, Segurança e Handoff**

### **4.1 Separação de Zonas Operacionais**

Todo repositório deve ser rigidamente dividido em três zonas para evitar que o ambiente vire um depósito de dumps ou artefatos temporários:  
src/          Aplicações reais, componentes operacionais e runtime do framework.  
public/       Assets públicos reais servidos pelo framework (ex: SVGs inline).  
supabase/     Migrations, schemas, triggers e policies do banco de dados operacional.  
docs/         Documentação ativa e arquitetura do projeto.  
\_references/  Insumos de design, investigações de mercado, workflows e referências visuais.  
\_artifacts/   Dumps de ferramentas, logs locais, builds antigos e exportações cruas.

**Isolamento no Build:** Arquivos em \_references/ e \_artifacts/ devem ser explicitamente ignorados no tsconfig.json, eslint.config.\*, .vercelignore e no mapeamento de @source do Tailwind CSS v4 para evitar quebras de compilação ou inchaço do bundle de produção.

### **4.2 Regra Absoluta Antisegredo**

* **NUNCA** versionar arquivos .env.local, service roles, chaves privadas ou tokens reais.  
* **NUNCA** registrar credenciais ativas em arquivos de log, relatórios de IA ou arquivos MEMORY.md. Todos os workflows exportados (ex: JSONs do n8n) devem utilizar placeholders textuais.  
* **Varredura Pré-Commit:** Executar obrigatoriamente uma varredura local por chaves vazadas antes de consolidar qualquer commit via comando regex:

rg \-n "service\_role|webhook\_token|Authorization|Bearer |apikey|pk\_\[A-Z0-9\_\]+|\[a-f0-9\]{64}" .

### **4.3 Resiliência e Integridade de Dados (Handoff)**

* **Persistência Primeiro:** Toda captura de dados (formulários, requisições de API, interações em terminais) deve salvar e persistir os dados no banco de dados local primeiro.  
* **Desacoplamento de Webhooks:** O disparo de webhooks, notificações ou integrações externas (n8n, CRMs, WhatsApp) deve ocorrer de forma assíncrona pós-persistência. Falhas na rede ou automações externas não podem resultar em perda de leads ou travamento da experiência do usuário.  
* **Rastreabilidade de Sincronização:** Schemas de tabelas integradas a serviços externos devem conter campos de controle nativos: sync\_status (enums: pending, success, failed) e sync\_error\_log para auditoria rápida.

## ---

**5\. Definition of Done (DoD) de Rota e Entregáveis**

Uma tarefa, funcionalidade ou página só será marcada como concluída se cumprir 100% dos seguintes critérios:

* **\[ \] Compilação Estrita:** npm run build (ou comando equivalente) executa sem erros de TypeScript, Linting ou alertas de variáveis globais quebras.  
* **\[ \] Aderência ao Design System:** Zero uso de Hexadecimais diretos no JSX. Uso exclusivo de tokens semânticos. Cantos secos aplicados (border-radius \<= 2px) e padding de segurança nos cabeçalhos display ativos.  
* **\[ \] Respiro Vertical Validado:** Layout livre de compressão visual desordenada. Aplicação de espaçamentos elegantes e intencionais (py-24, py-36).  
* **\[ \] SEO Técnico & Metadados:** Injeção automatizada de metadados via helpers dedicados (buildMetadata), limitando títulos a 60 caracteres e descrições a 155 caracteres. Presença obrigatória de tags estruturadas JSON-LD (personSchema, organizationSchema, websiteSchema).  
* **\[ \] Métricas de Lighthouse Portadas:**  
  * *Performance:* \>= 90 (fontes locais self-hosted, otimização nativa de imagens).  
  * *Acessibilidade:* \>= 95 (contraste mínimo WCAG AA de 4.5:1, navegação por teclado funcional, aria-label em botões iconográficos).  
  * *Melhores Práticas:* \>= 95 (zero erros em runtime no console, HTTPS).  
  * *SEO:* \>= 95 (canonical tags ativas, sitemap dinâmico estruturado).

## ---

**6\. Apêndice: Padrões de Código Homologados (Gabarito para IA)**

### **6.1 A Camada de Tokens de Dados Compartilhados (Shared Schema)**

// packages/shared/src/schemas/user.ts  
import { z } from 'zod';

export const UserSchema \= z.object({  
  id: z.string().uuid(),  
  name: z.string().min(2),  
  email: z.string().email(),  
  role: z.enum(\['USER', 'ADMIN'\]),  
});

export type User \= z.infer\<typeof UserSchema\>;

### **6.2 O Padrão de Serviço Backend (SRP & Persistência Primeiro)**

// apps/backend/src/services/user.service.ts  
import { UserSchema, User } from '@my-project/shared';  
import { prisma } from '../infrastructure/db';

export class UserService {  
  async createUser(data: unknown): Promise\<User\> {  
    // Validação Atômica do Contrato  
    const validatedData \= UserSchema.parse(data);   
      
    // Regra de Ouro: Persistência no Banco Local Primeiro  
    const newUser \= await prisma.user.create({   
      data: {  
        ...validatedData,  
        sync\_status: 'pending'  
      }  
    });  
      
    return newUser;  
  }  
}

### **6.3 O Consumo Componentizado no Frontend (Atoms & Tokens)**

// apps/frontend/src/components/user-card.tsx  
import { User } from '@my-project/shared';  
import { Card, Badge } from '@/components/ui'; // Componentes Átomos (Shadcn)

interface UserCardProps {  
  user: User; // Consumo direto do token de dados compartilhado  
}

export function UserCard({ user }: UserCardProps) {  
  return (  
    \<Card className="p-4 rounded-sm border-black-line bg-architectural-black"\>  
      \<h3 className="text-lg font-bold text-warm-off-white tracking-tight"\>  
        {user.name}  
      \</h3\>  
      \<p className="text-sm text-muted-foreground"\>{user.email}\</p\>  
      \<Badge variant={user.role \=== 'ADMIN' ? 'destructive' : 'secondary'}\>  
        {user.role}  
      \</Badge\>  
    \</Card\>  
  );  
}

## ---

**7\. Orquestradores Avançados de Agentes (Super-Prompts)**

### **7.1 Prompt de Arquitetura Frontend & UI**

Act like a Senior Frontend Architect & Design Systems Lead. Your mission is to evolve the current repository using the "Atomic & Tokenized" methodology detailed in the system's core guidelines.

\=========================================  
1\. AUTO-DISCOVERY & EVIDENCE (STRICT)  
\=========================================  
\- DO NOT ask me to paste code. Explore the file tree.  
\- Identify: React/Next.js version, Tailwind version (v3 vs v4), shadcn presence, and state management.  
\- Every suggestion must point to the specific file and line: \`\[path/to/file.tsx:L42\]\`.

\=========================================  
2\. CORE OBJECTIVES: TOKENIZE & ATOMIZE  
\=========================================  
A) DESIGN TOKENS (The Source of Truth):  
\- Audit \`tailwind.config\` or CSS variables.  
\- Propose a 3-tier hierarchy: Primitive (Scale) \-\> Semantic (Purpose) \-\> Component (Specific).  
\- If on Tailwind v4: Transition to CSS-first variables using @theme and OKLCH for perceptually uniform colors, completely removing hardcoded hex values from JSX.  
\- Enforce the restricted palette: Fundo Primário (\#0A0A0A), Texto Principal (\#F7F7F7), and Acento (Amber \#D4A843). Green/Teal variants are strictly forbidden.

B) ATOMIC REFACTORING:  
\- Atoms: Review \`components/ui\`. Ensure Radix UI primitives are used correctly (a11y, focus-visible) and border-radius never exceeds 2px (rounded-sm). Enforce a padding-block of 0.08em for uppercase Barlow Condensed headers.  
\- Molecules/Organisms: Identify patterns like Forms, Modals, and Cards. Refactor using CVA (Class Variance Authority) for clean variants.  
\- Component Ownership: Ensure \`cn(clsx \+ tailwind-merge)\` is used for all style overrides.

C) PERFORMANCE & A11Y (WCAG 2.2):  
\- Audit for Cumulative Layout Shift (CLS) in components.  
\- Ensure 'sr-only' for icon-only buttons and proper ARIA states.

\=========================================  
3\. OUTPUT FORMAT  
\=========================================  
1\. Current State: What you found (Frameworks/Versions).  
2\. Critical Debt: Inconsistent tokens, hardcoded values, or incorrect border-radius elements.  
3\. Implementation Plan: Incremental steps to atomize the UI without breaking changes.

### **7.2 Prompt de Engenharia Backend & Reuso**

Act like a Senior Backend Architect & Staff Engineer. Your goal is to apply "Componentization and Modularization" to the server logic, integration layer, and database architecture.

\=========================================  
1\. ARCHITECTURAL AUDIT (STRICT)  
\=========================================  
\- DO NOT ask for code. Explore the repo to identify: Runtime (Node/Bun/Go/Python), Framework, ORM, and API Pattern (REST/GraphQL/gRPC).  
\- Map the folder structure: Are we using Hexagonal, Clean, or a Monolithic pattern?

\=========================================  
2\. CORE OBJECTIVES: MODULARIZE & CONTRACT  
\=========================================  
A) BACKEND "COMPONETIZATION" (Service Pattern):  
\- Identify business logic leaked into Controllers/Routes.  
\- Propose refactoring into "Atomic Services": Small, single-responsibility units that are highly reusable.  
\- Audit Dependency Injection: Are components tightly coupled? Suggest Interfaces/Contracts.  
\- Enforce the "Persistence First" rule: ensure inbound payloads are fully validated and safely written to the local database before invoking external webhooks or automation pipelines (e.g., n8n).

B) "TOKENIZATION" (Shared Schemas & DTOs):  
\- Audit data validation (Zod, TypeBox, Pydantic).   
\- Ensure "Single Source of Truth" for types: One schema defining the DB, the API response, and the Frontend contract.  
\- Propose Shared Utils for common logic (Error handling, Logging, Auth Middlewares).  
\- Check tables for synchronization tracking fields (\`sync\_status\` and \`sync\_error\_log\`).

C) DX & SCALABILITY:  
\- Audit Database indexing, security policies (RLS if on Supabase), and Query performance based on the ORM usage found.  
\- Review Error Handling: Ensure it is structured and consistent across all units, never revealing raw API keys or internal secrets in logs or responses.  
\- Ensure strict TypeScript/Typing usage.

\=========================================  
3\. OUTPUT FORMAT  
\=========================================  
1\. Infrastructure Map: Current architecture and bottlenecks found.  
2\. Refactor Proposal: How to break down monolithic logic into "Atomic Services" ensuring data resilience.  
3\. Contract Alignment: How to sync backend "tokens" (types/schemas) with the rest of the system.  
