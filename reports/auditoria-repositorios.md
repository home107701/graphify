# Auditoria dos repositórios GitHub — @home107701

**Data da revisão:** 17/11/2026 · **Fonte:** API do GitHub (metadados, upstream, comparativo de commits, linguagens)
**Escopo:** 28 repositórios · todos forks · 0 privados · 0 arquivados · 0 com issues ou PRs abertos

---

## 1. Resumo executivo

A conta @home107701 tem **28 repositórios**, criados quase todos em uma única janela: 5 em outubro/2026 e **23 em novembro/2026**. Não existe um único repositório original — **100% são forks de terceiros**, sem nenhum commit próprio no branch padrão de qualquer um deles. Na prática, a conta funciona hoje como uma **biblioteca pessoal curada de ferramentas de IA**, não como um portfólio de código autoral.

O acervo é coerente e tem um eixo claro: **IA aplicada com custo zero**. Os temas dominantes são agent skills/prompts (8 repos), gateways e APIs gratuitas de LLM (3), tooling de desenvolvimento e engenharia de código assistida por agente (4), jurídico e dados públicos brasileiros (3), automação de mídia/vídeo (3), bots e hardware (3) e educação/pesquisa (4). O upstream somado desses projetos é de **~1,30 milhão de estrelas** — são projetos grandes, comunitários e, em vários casos, de referência (microsoft/markitdown, github/github-mcp-server, rea/morluto, google/skills).

O ponto crítico é a **manutenção**: apenas **12 dos 28 forks estão sincronizados** com o upstream. **15 estão atrasados** e 1 divergiu. Em quatro casos o atraso é material — rea (-1.616 commits), OmniRoute (-880), OpenMausBot (-776) e graphify (-473) —, o que significa que essas cópias carregam bugs, CVEs e funcionalidades já corrigidas lá na origem. Há ainda um risco silencioso de **perda de trabalho**: `awesome-freellm-apis` tem 2 commits autorais (um kit de agente "Olavo de Carvalho") que vivem apenas em um branch secundário `arena/718d4cf2-awesome-freellm-apis`, invisível no branch padrão e a 235 commits atrás do upstream.

Três observações de higiene completam o quadro: **nenhum** dos 28 repositórios tem topics configurados (busca e organização internas ficam cegas), três não têm linguagem detectada (projetos essencialmente de dados/conteúdo: leis-BR, awesome-freellm-apis, notebooklm-para-concursos) e um está acima de 8 GB de disco (`leis-BR-frk`), o que encarece clonar e inviabiliza uso em CI.

**Recomendação em uma frase:** preservar o acervo como está (ele é bom), mas transformá-lo de "pilha de clones esquecidos" em "biblioteca viva" — sincronizar o que é usado, arquivar o que é morto, promover o trabalho autoral a repositório próprio e adicionar topics/licença explícita.

### Indicadores

| Indicador | Valor |
|---|---|
| Repositórios totais | 28 |
| Repositórios originais (não-fork) | 0 |
| Forks sincronizados com upstream | 12 (43%) |
| Forks atrasados | 15 (54%) |
| Forks divergidos | 1 |
| Commits autorais (fora do branch padrão) | 2 (em 1 repositório) |
| Estrelas somadas dos upstreams | ~1,30 mi |
| Issues abertas / PRs abertos | 0 / 0 |
| Repositórios com topics | 0 |
| Repositórios sem linguagem detectada | 3 |
| Licença detectada pelo GitHub (SPDX) | 0 de 28 (arquivo LICENSE presente, tipo não reconhecido) |
| Maior repositório | leis-BR-frk — 8,2 GB |

### Prioridades sugeridas

| # | Ação | Por quê | Repos afetados |
|---|---|---|---|
| 1 | Sincronizar (sync fork) os forks em uso | Correções de segurança e features já existem no upstream | rea-fork, OmniRoute, OpenMausBot, graphify, skills, freellmapi-frk, photo-frame-dashboard-fork, Fork-free-claude-code, skills-frk, github-mcp-server, markitdown, Advocacia-Aberta, osint-brazuca, spellbook-fork, LetsFG-frk |
| 2 | Resgatar os 2 commits autorais de `awesome-freellm-apis` | Trabalho autoral só existe em branch secundário, sem PR aberto | awesome-freellm-apis |
| 3 | Arquivar forks não utilizados | Reduz ruído e superfície de manutenção | candidatos listados na seção 3 |
| 4 | Padronizar topics, descrição e licença | Descoberta, organização e conformidade | 28 / 1 / 28 |
| 5 | Tratar repositórios gigantes | 8,2 GB e 3,5 GB inviabilizam clone em CI | leis-BR-frk, OmniRoute |

---

## 2. Visão por categoria

| Categoria | Repos | Estrelas (upstream) | Em dia | Atrasados | Divergiu | Leitura |
|---|---|---|---|---|---|---|
| **Agent Skills & Prompts** | 8 | ~232 mil | 4 | 4 | 0 |
| **LLM APIs & Gateways gratuitos** | 3 | ~148 mil | 0 | 2 | 1 |
| **Dev tooling, MCP & engenharia de código** | 4 | ~847 mil | 0 | 4 | 0 |
| **Jurídico & dados públicos BR** | 3 | ~6 mil | 1 | 2 | 0 |
| **Mídia, vídeo & automação de conteúdo** | 3 | ~41 mil | 3 | 0 | 0 |
| **Bots, automação & hardware** | 3 | ~29 mil | 1 | 2 | 0 |
| **Educação, pesquisa & utilitários** | 4 | ~2 mil | 3 | 1 | 0 |
| **Total** | **28** | **~1,30 mi** | **12** | **15** | **1** |

### Como ler cada categoria

**Agent Skills & Prompts** — 8 repositórios. É o coração do acervo: ferramentas que ensinam agentes (Claude Code, Codex, Cursor) a produzir artefatos específicos — diagramas SVG, isométricos, ilustrações. Sete dos oito vêm de projetos com forte tração; o único pequeno é diagrammer (4 estrelas no upstream). O item mais estratégico é Fork-free-claude-code, que destrava acesso gratuito a múltiplos harnesses de IA.

**LLM APIs & Gateways gratuitos** — 3 repositórios. Concentra a tese de "IA a custo zero": gateways que unificam centenas de provedores e endpoints gratuitos atrás de uma única API compatível com OpenAI. Aqui está o maior atraso relativo do acervo (OmniRoute, -880 commits) e o único caso de divergência com trabalho autoral.

**Dev tooling, MCP & engenharia de código** — 4 repositórios. Projetos grandes e maduros, com quase todas as estrelas do acervo somado (~846 mil). São ferramentas de infraestrutura — MCP oficial do GitHub, conversão de documentos para Markdown, knowledge graph de código e engenharia reversa. Justamente por serem maduros, ficam rapidamente defasados: todos os quatro estão atrasados.

**Jurídico & dados públicos BR** — 3 repositórios. A única vertente genuinamente local: método jurídico executável por agentes, base de leis brasileiras e OSINT focado no Brasil. Dois estão sincronizados ou quase; o risco aqui não é técnico, é de tamanho — leis-BR ocupa 8,2 GB.

**Mídia, vídeo & automação de conteúdo** — 3 repositórios. Automação de ponta a ponta para produção de vídeo: narração, cortes, publicação e monetização. Curiosamente é a categoria mais saudável — todos sincronizados —, mas também a mais estagnada no upstream (ShortGPT sem atualização desde fevereiro/2025).

**Bots, automação & hardware** — 3 repositórios. A vertente "físico/operacional": bot com VM, launcher que instala apps a partir de releases do GitHub e hack de tablets/frames Android. Mistura um projeto muito ativo e defasado (OpenMausBot) com dois utilitários estáveis.

**Educação, pesquisa & utilitários** — 4 repositórios. Ferramentas de apoio: engenharia de estudo com NotebookLM, API de livros, busca de voos/hotéis e visualizador odontológico. É a cauda longa do acervo — pequena, estável e de nicho.

---

## 3. Inventário detalhado

Ordenado por categoria. "Status" compara o branch padrão do fork com o upstream no momento da auditoria.

### Agent Skills & Prompts

| Repositório | Upstream | Stack | Status | Último commit | Tamanho | O que é |
|---|---|---|---|---|---|---|
| [`Fork-free-claude-code`](https://github.com/home107701/Fork-free-claude-code) | Alishahryar1/free-claude-code | Python:95% | -47 | 2026-10-31 | 16 MB | Use Claude Code, Codex, Antigravity, VSCode, Pi, and OpenCode (and 6 other harnesses) for free (1.3B+ free … |
| [`diagram-design-frk`](https://github.com/home107701/diagram-design-frk) | cathrynlavery/diagram-design | HTML:58% | em dia | 2026-11-12 | 38 MB | Editorial diagram design for Claude Code, Codex, GitHub Copilot, Cursor, Factory Droid, Qoder, and Pi. 45 d… |
| [`skills`](https://github.com/home107701/skills) | vercel-labs/skills | TypeScript:100% | -81 | 2026-10-29 | 2 MB | The open agent skills tool - npx skills |
| [`anatomy-frk`](https://github.com/home107701/anatomy-frk) | wheresryan22/anatomy | JavaScript:94% | em dia | 2026-10-18 | 13 MB | An agent skill for creating detailed, interactive isometric illustrations of real-world machines and comple… |
| [`skills-frk`](https://github.com/home107701/skills-frk) | google/skills | Python:84% | -31 | 2026-11-14 | 6 MB | Agent Skills for Google products and technologies |
| [`svg-diagram-frk`](https://github.com/home107701/svg-diagram-frk) | bybit-exchange/svg-diagram | JavaScript:100% | em dia | 2026-09-03 | 537 KB | Agent skill that draws architecture, flowchart, sequence, data-flow and lifecycle diagrams as hand-placed S… |
| [`spellbook-fork`](https://github.com/home107701/spellbook-fork) | majiayu000/spellbook | Python:65% | -2 | 2026-11-15 | 6 MB | Cross-runtime skills for Claude Code, Codex, and multi-agent workflows. |
| [`diagrammer-frk`](https://github.com/home107701/diagrammer-frk) | Anish-Reddy-K/diagrammer | Python:100% | em dia | 2026-11-06 | 365 KB | Claude Code skill and Python CLI for generating clean blueprint-style SVG diagrams from JSON specs. |

### LLM APIs & Gateways gratuitos

| Repositório | Upstream | Stack | Status | Último commit | Tamanho | O que é |
|---|---|---|---|---|---|---|
| [`OmniRoute`](https://github.com/home107701/OmniRoute) | cheaper-inference/OmniRoute | TypeScript:95% | -880 | 2026-11-14 | 3,5 GB | Never stop coding. Free MIT AI gateway: one endpoint, 375 providers (150+ free), 1,400+ models Kimi, Claude… |
| [`freellmapi-frk`](https://github.com/home107701/freellmapi-frk) | tashfeenahmed/freellmapi | TypeScript:99% | -74 | 2026-11-06 | 24 MB | 7,4 billion tokens per month. 34 free LLM providers. 635 free model endpoints. All behind one /v1 endpoint,… |
| [`awesome-freellm-apis`](https://github.com/home107701/awesome-freellm-apis) | open-free-llm-api/awesome-freellm-apis | dados/conteúdo | divergiu (+213/-235) | 2026-11-12 | 542 KB | 134+ free LLM APIs & AI API keys from 40+ providers. Google Gemini, NVIDIA NIM, Groq, OpenRouter & more. On… |

### Dev tooling, MCP & engenharia de código

| Repositório | Upstream | Stack | Status | Último commit | Tamanho | O que é |
|---|---|---|---|---|---|---|
| [`rea-fork`](https://github.com/home107701/rea-fork) | morluto/rea | TypeScript:91% | -1616 | 2026-11-05 | 138 MB | Reverse engineer anything with agents, from app behavior down to native binaries. |
| [`markitdown`](https://github.com/home107701/markitdown) | microsoft/markitdown | Python:100% | -3 | 2026-10-28 | 6 MB | Python tool for converting files and office documents to Markdown. |
| [`graphify`](https://github.com/home107701/graphify) | Graphify-Labs/graphify | Python:100% | -473 | 2026-10-27 | 32 MB | Tokens.Economy...Turn any codebase, with its docs, SQL schemas, configs, and PDFs, into a queryable knowled… |
| [`github-mcp-server`](https://github.com/home107701/github-mcp-server) | github/github-mcp-server | Go:96% | -9 | 2026-10-30 | 56 MB | GitHub's official MCP Server |

### Jurídico & dados públicos BR

| Repositório | Upstream | Stack | Status | Último commit | Tamanho | O que é |
|---|---|---|---|---|---|---|
| [`leis-BR-frk`](https://github.com/home107701/leis-BR-frk) | ctresb/leis | dados/conteúdo | em dia | 2026-11-02 | 8,2 GB | Todas as leis do Brasil |
| [`osint-brazuca-frk`](https://github.com/home107701/osint-brazuca-frk) | osintbrazuca/osint-brazuca | Python:98% | -3 | 2026-10-26 | 6 MB | Repositório criado com intuito de reunir informações, fontes(websites/portais) e tricks de OSINT dentro do … |
| [`advocacia-aberta_fork`](https://github.com/home107701/advocacia-aberta_fork) | emidio-trancoso/advocacia-aberta | Python:59% | -3 | 2026-11-02 | 48 MB | Método jurídico aberto e executável por agentes de IA: base curada de STF/STJ, legislação, súmulas, temas e… |

### Mídia, vídeo & automação de conteúdo

| Repositório | Upstream | Stack | Status | Último commit | Tamanho | O que é |
|---|---|---|---|---|---|---|
| [`MoneyPrinterV2`](https://github.com/home107701/MoneyPrinterV2) | FujiwaraChoki/MoneyPrinterV2 | Python:97% | em dia | 2026-09-15 | 447 KB | Automate the process of making money online. |
| [`video-ShortGPT`](https://github.com/home107701/video-ShortGPT) | RayVentura/ShortGPT | Python:100% | em dia | 2025-02-10 | 4 MB | 🚀🎬 ShortGPT - Experimental AI framework for youtube shorts / tiktok channel automation |
| [`video-ffmpeg-ai`](https://github.com/home107701/video-ffmpeg-ai) | numbpill3d/ffmpeg-ai | Python:100% | em dia | 2026-11-02 | 6 MB | Python CLI for generating narrated short-form and landscape videos with free AI services and FFmpeg. |

### Bots, automação & hardware

| Repositório | Upstream | Stack | Status | Último commit | Tamanho | O que é |
|---|---|---|---|---|---|---|
| [`OpenMausBot`](https://github.com/home107701/OpenMausBot) | milind-soni/OpenMausBot | TypeScript:90% | -776 | 2026-11-15 | 550 MB | Open-source Grok Bot alternative with a virtual machine that bots can use |
| [`Emulador-GithubLauncher`](https://github.com/home107701/Emulador-GithubLauncher) | SirDiabo/GithubLauncher | C#:100% | em dia | 2026-11-06 | 10 MB | A Launcher that Downloads and Updates Applications from Github Releases |
| [`photo-frame-dashboard-fork`](https://github.com/home107701/photo-frame-dashboard-fork) | wesbos/photo-frame-dashboard | Python:51% | -51 | 2026-11-04 | 10 MB | Getting ADB, root, backups and custom apps onto locked-down Android photo frames (Skylight Calendar, BIUFRAME) |

### Educação, pesquisa & utilitários

| Repositório | Upstream | Stack | Status | Último commit | Tamanho | O que é |
|---|---|---|---|---|---|---|
| [`LetsFG-frk`](https://github.com/home107701/LetsFG-frk) | LetsFG/LetsFG | Python:39% | -2 | 2026-11-01 | 58 MB | Agent-native flight & hotel search and booking — MCP server, CLI, and Python/JS SDKs. Every airline in the … |
| [`notebooklm-para-concursos-frk`](https://github.com/home107701/notebooklm-para-concursos-frk) | gilsonnogueira/notebooklm-para-concursos | dados/conteúdo | em dia | 2026-10-11 | 3 MB | Ecossistema de Engenharia de Estudos com IA Fundamentada (NotebookLM + Gemini Estudantes). Metodologia N.A.… |
| [`FreeBooksAPI-frk`](https://github.com/home107701/FreeBooksAPI-frk) | Rickaym/FreeBooksAPI | Python:98% | em dia | 2023-08-26 | 714 KB | A comprehensive (unofficial) API service for planet-ebooks, libgen/gen.lib.rus.ec, and libgen.lc, providing… |
| [`dental-scan-viewer`](https://github.com/home107701/dental-scan-viewer) | Tatendaz/dental-scan-viewer | HTML:58% | em dia | 2026-11-01 | 33 MB | — |

---

## 4. Riscos e pontos de atenção

| Risco | Evidência | Impacto | Mitigação |
|---|---|---|---|
| Defasagem de segurança | 15 forks atrás do upstream; rea -1.616, OmniRoute -880, OpenMausBot -776, graphify -473 | Dependências e correções não aplicadas; CVEs conhecidas podem persistir | Habilitar "Sync fork" e revisar releases; priorizar os 4 mais atrasados |
| Perda de trabalho autoral | 2 commits de `home107701` só no branch `arena/718d4cf2-awesome-freellm-apis`, sem PR | Trabalho invisível no branch padrão e em risco em qualquer reset | Abrir PR para o upstream ou extrair para repositório próprio |
| Ausência de código original | 0 repositórios não-fork | Portfólio não demonstra autoria; contribuições ficam diluídas | Promover os projetos autorais a repos próprios com README próprio |
| Peso de repositório | leis-BR 8,2 GB; OmniRoute 3,5 GB; OpenMausBot 550 MB | Clone lento, inviável em CI/containers, cota de armazenamento | Usar clone raso (`--depth 1`) ou sparse-checkout; não versionar dados baixados |
| Descoberta e organização | 0 de 28 com topics; 1 sem descrição; 3 sem linguagem detectada | Busca interna, filtros e SEO do perfil ficam inúteis | Adicionar 3–5 topics por repo e padronizar descrição |
| Licença ambígua | LICENSE presente em todos, mas GitHub não identifica SPDX em nenhum | Risco jurídico ao reutilizar/distribuir | Manter o arquivo do upstream intacto e declarar a licença no README |

---

## 5. Plano de ação em 30 dias

**Semana 1 — conter risco.** Sincronizar os quatro forks mais atrasados (rea, OmniRoute, OpenMausBot, graphify) e abrir PR com os commits do agente "Olavo de Carvalho".

**Semana 2 — limpar.** Arquivar forks ociosos e duplicados (os pares `skills`/`skills-frk`, os três `*-fork` de diagramação, `FreeBooksAPI-frk`, `video-ShortGPT`). Manter apenas o que é efetivamente usado.

**Semana 3 — organizar.** Adicionar topics e descrição em todos os 28; corrigir a detecção de licença; resolver o peso de `leis-BR-frk` (dados fora do Git ou clone raso documentado).

**Semana 4 — publicar.** Extrair o trabalho autoral para repositórios próprios — o agente de persona é o candidato mais forte, por já ter estrutura de RAG, evals e curadoria de fontes. Isso converte a biblioteca em portfólio.

---

*Metodologia: coleta via GitHub CLI/API em 17/11/2026 — `gh repo list` para metadados, endpoint de compare (`upstream:branch...fork:branch`) para o status de sincronização, `/languages` e `/contents` para stack e higiene. Estrelas referem-se ao repositório upstream, não ao fork.*