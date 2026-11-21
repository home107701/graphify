# Relatório FASE 1 — DRY RUN (somente leitura)
**Reorganização do Google Drive — sem exclusões, sem alterações antes da aprovação**

> **Data da varredura:** 2026-11-21 10:45 UTC (reexecutada em 2026-11-21 11:00 UTC para subpasta “A Ordem e o Palco”)  
> **Conta:** homebox765@gmail.com (Home BOXTV) — owner `14624453573526187579`  
> **Branch:** `arena/dc87a1d4-graphify` de `0a8cd4e1e342235fe53e881fb5d591bf0460071f` (v8)  
> **Modo:** somente leitura — nenhuma pasta/arquivo foi criado, movido, renomeado ou excluído. 0 shared drives (confirmado via `list_drives`).

---

## 1. Inventário completo

- **Total de itens verificados (recursivo): 337**  
  - Pastas: ~56 (12 na raiz + 11 em 01 + 3 em 02 + 4 em 03 + 3 em 04 + 2 em 05 + 6 em 06 + 2 em 07 + 4 em 08 + 1 em 09 + 3 em 99 + A Ordem e o Palco + subpastas Onlyoffice)
  - Arquivos: ~281
  - Atalhos: 10 (Livros, Radiologia Oral, Terapias Atuais, NETTER, Caminhos da Polpa, Cirurgia, Editais, ABO_Aperf-2026, Concursos, etc.)
  - Arquivos de sistema: 3 (`.DS_Store` + `2026-11-03_DS_Store.bin`)

- **Raiz (`Meu Drive`, ID `0ACH0E8hRSHWyUk9PVA`): 35 itens** — 12 pastas + 23 arquivos soltos (detalhados abaixo).  
  Todas as pastas raiz criadas em 2026-11-09 e pertencem a você.

- **Pastas vazias detectadas (estrutura a manter):** `01.4 — Livros, Tratados e Acervo`, `04.1 — Acervo Geral`, `06.2 — Planilhas e Dados`, `26-11_Arena — arquivo de trabalho (esvaziada)`, `PDFs2026` (×2), `Cedula-Dolar` (×2), 3 subpastas Onlyoffice-P-Aulas-Odonto MAIS RECENTE.

- **Cobertura:** cada item listado com `ID, nome, tipo, tamanho (se disponível), localização atual, data da última modificação, owner, compartilhado` — ver `inventario_completo.csv` (337 linhas, ordenado por localização).

### 1.1 Arquivos soltos na raiz — 23 itens que devem sair da raiz
| Arquivo | Tipo | Tamanho | Data |
|---|---|---|---|
| Exodontia Editorial — 20 slides.pptx | pptx | 69364 | 2026-11-20 |
| exodontia-terceiros-molares.pptx | pptx | 112462 | 2026-11-20 |
| Exodontia de Terceiros Molares — Bloco 1 (Slides 021–040) | gslides | 32195 | 2026-11-20 |
| Exodontia_Terceiros_Molares_Bloco1_Slides_021_040.pptx | pptx | 72582 | 2026-11-20 |
| Exodontia de Terceiros Molares — Bloco 1 (Slides 021–040) (2ª cópia) | gslides | 3666 | 2026-11-20 |
| ppt-impeccable — Exodontia de terceiros molares (R061).pptx | pptx | 932593 | 2026-11-20 |
| Exodontia de Terceiros Molares — Slides 041–080 | gslides | 2420348 | 2026-11-18 |
| Tracionamento guiado por imagem — Módulo 2 | gslides | 161599 | 2026-11-18 |
| 126-20261118-0000 \| Diagnóstico de Patologias dos Maxilares | gslides | 5417 | 2026-11-18 |
| 081_2026-11-18_0043 | gslides | 18283 | 2026-11-18 |
| Tracionamento Ortodôntico-Cirúrgico… — Módulo 2 | gslides | 11611 | 2026-11-18 |
| Tracionamento… — Módulo 2 (Slides 081–125) | gslides | 31399 | 2026-11-18 |
| Diagnóstico de Patologias dos Maxilares — Slides 126–165 | gslides | 31399 | 2026-11-18 |
| Diagnóstico de Patologias dos Maxilares — Slides 126–165 (cópia) | gslides | 3666 | 2026-11-18 |
| Aula-slides-2ed-26-11-17.pptx | pptx | 23119969 | 2026-11-17 |
| Aula-slides-2ed-26-11-17-especificacao.md | md | 59026 | 2026-11-17 |
| DiaDeSorte_Padroes_Favoritos_e_Zebra_1320-1349_17-11-2026.pptx | pptx | 220047 | 2026-11-17 |
| Aula-imagem-slides-26-11-17.pptx | pptx | 5622313 | 2026-11-17 |
| Aula-imagem-26-17.docx | docx | 58605 | 2026-11-17 |
| ATM — degeneração e as duas saídas | gslides | 1585050 | 2026-11-15 |
| O mínimo que você precisa saber para não ser um idiota.md | md | 1343959 | 2026-11-15 |
| analise-provas-repositorio.zip | zip | 27011 | 2026-11-14 |
| Gerador de Combinatórias — Cobertura Uniforme (Lotofácil).docx | docx | 40821 | 2026-11-12 |

Todos já possuem prefixo de data ou terão destino em `00 — Triagem` → `01.3`/`06.1`/`04.1` conforme `plano_movimentacao.csv`.

---

## 2. Árvore de pastas proposta
Ver `arvore_proposta.md` — estrutura 00 a 09 + Aulas/comandos + **D-Duplicados** (sucede `99 — Duplicados (nada foi apagado)` por renomeação, preservando ID `1sC9IMFSDSLXF9roRqVhZd54gofXP2Q55`).

**Novidades:**
- `00 — Triagem` (novo, raiz) — ponto de entrada dos 23 soltos; esvaziado após mover.
- `D-Duplicados/` com subpastas temáticas: `01-Odonto — TCLE e Contratos`, `06-Pesquisa — Onlyoffice`, `03-Cursos — Onlyoffice`, `99.1 — Cópias excedentes`, `Onlyoffice-26-11-02 — DUPLICADO`, `_legado-tecnico`.
- Todo o restante mantido — nenhuma pasta excluída.

---

## 3. Plano de movimentação (CSV)
**Arquivo:** `plano_movimentacao.csv` — 337 linhas + cabeçalho, colunas `ID, nome, tipo, localização atual, localização proposta, ação, justificativa`.

### Contagem por ação (DRY RUN)
| Ação | Qtd | Significado |
|---|---|---|
| **manter** | 192 | Pasta/arquivo já no lugar correto |
| **nao alterar — item de terceiros** | 47 | Conteúdo de `diogorego@gmail.com` em `08` — exige sua autorização |
| **manter — compartilhado** | 30 | Seus arquivos em `08` compartilhados com terceiros — preserva links |
| **mover** | 23 | 23 soltos da raiz → `00 — Triagem` → `01.3`/`06.1`/`04.1` |
| **manter em D-Duplicados** | 14 | Duplicatas já em `99` — re-rotular sob `D-Duplicados` |
| **manter — atalho** | 10 | Atalhos para pastas externas — não mover |
| **manter — revisar futura consolidacao** | 7 | `Aulas/` — manter até decidir fusão com `01.3` |
| **manter — vazia** | 6 | Pastas vazias estruturais |
| **manter — consolidar futuro** | 4 | Pastas Onlyoffice MAIS RECENTE (vazias ou em transição) |
| **manter — legado 2018** | 2 | `Medicamentos`, `Ebooks OL` |
| **mover para D-Duplicados** | 2 | `.DS_Store` → `D-Duplicados/_legado-tecnico` |
| **renomear/padronizar** | 1 | `99 — Duplicados` → `D-Duplicados` (mesmo ID) |

**Exemplos de linhas (primeiras do CSV):**
```
081_2026-11-18_0043, mover, Meu Drive → Meu Drive/00 — Triagem, Arquivo solto sem pasta definida
Exodontia Editorial — 20 slides.pptx, mover, Meu Drive → Meu Drive/01 — Odontologia e Saúde/01.3 — Aulas, Imaginologia e Mídia, Slides de Exodontia solto
...
01 — RADIOLOGIA — Abertura: Da imagem à decisão — 15 slides, manter, já em RADIOLOGIA, Pasta na localização correta
```

> **Renomeação Fase 2:** `AAAA-MM-DD-Nome-assunto.ext` somente quando data segura (ex.: todos os `2026-XX-YY_*` já ok). Se data não determinável com segurança (ex.: `081_2026-11-18_0043` sem contexto, `Super Bomberman` 1996), **manter nome atual e sinalizar** — ver `duplicatas_revisao.csv`.

---

## 4. Duplicatas identificadas

### 4.1 Grupos confirmados — 14 grupos, 28 arquivos (mesmo nome normalizado + mesmo tamanho)
**Arquivo:** `duplicatas.csv` — cada grupo com `manter — mais recente (canônico)` em `01/06/03` e `mover para D-Duplicados — mais antiga` em `99`/`D-Duplicados`.

| Grupo | Tamanho | Qtd | Canônico (manter) | Duplicata (mover) |
|---|---|---|---|---|
| aulas od | 28845 | 2 | `2026-06-27_Aulas-Od.docx` em `06.1` | `Aulas-Od.docx` em `99/.../Onlyoffice-2026-08 — cópia` |
| contrato de prestacao de servicos profissionais | 42105 | 2 | `2026-11-09_CONTRATO_...` em `01.1` | `..._MAIS_RECENTE.docx` em `99.1` |
| contrato implante ms lgpd cro 20 paginas | 3896722 | 2 | `...Contrato_Implante...pdf` em `01.1` | `..._MAIS_RECENTE.pdf` em `99.1` |
| novo documento | 8504 | 2 | `2026-08-13_Novo_documento.docx` em `06.1` | `Novo documento.docx` em `99/.../Onlyoffice-2026-08` |
| obsidian knowledge pipeline | 16829227 | 2 | `...Obsidian_Knowledge_Pipeline.pptx` em `06.1` | `..._D053_...pptx` em `99.1` |
| prp aulas 26 10 c | 30788 | 2 | `2026-10-13_Prp-Aulas-26-10-C.docx` em `06.1` | `Prp-Aulas-26-10-C.docx` em `99/.../Onlyoffice-2026-08` |
| sites ia | 46498 | 2 | `2026-07-08_Sites-IA.docx` em `06.1` | `Sites-IA.docx` em `99/.../Onlyoffice-2026-08` |
| tcle exod protocolo | 91221 | 2 | `..._MAIS_RECENTE.pdf` em `01.1` | `..._D070_...pdf` em `99.1` |
| tcle tracionamento | 23025 | 2 | `..._MAIS_RECENTE.docx` em `01.1` | `..._D074_...docx` em `99.1` |
| v2 prpt convert ilustracao ref | 28372 | 2 | `..._V2-Prpt-...` em `06.1` | `V2-Prpt-...` em `99/...` |
| v2 prpt converter vetor em ultrarealista ref | 28860 | 2 | `..._V2-Prpt-Converter...` em `06.1` | `V2-Prpt-Converter...` em `99/...` |
| + 3 grupos de terceiros (ROMs) | 2097152/524800 | 2 cada | manter em `08 — Compartilhado/ROM_SNES` | sinalizar — terceiros, não mover sem autorização |

**Regra segura:** mesmo nome normalizado + mesmo `size` em bytes + localizações distintas (canônico em `01/06/03` vs cópia em `99`) → manter canônico, mover só a mais antiga para `D-Duplicados` em subpasta temática. Conteúdo e IDs preservados (movimento via `parents`).

### 4.2 Grupos suspeitos — 10 grupos, ~20 arquivos — **NÃO MOVER, sinalizar para revisão**
**Arquivo:** `duplicatas_revisao.csv` — mesmo nome normalizado mas **tamanhos diferentes**, impossível determinar com segurança qual é a mais recente sem abrir conteúdo.

Exemplos:
- **Exodontia Bloco 1 (Slides 021–040)**: `32195B` (gslides 02:51:09) vs `72582B` (pptx 02:51:08) vs `3666B` (gslides 02:51:00) — tamanhos distintos, não mover.
- **Tracionamento Módulo 2**: `161599B` vs `11611B` vs `31399B` — variantes de módulo, não mover.
- **Diagnóstico 126–165**: `31399B` vs `3666B` — idem, mais `5417B` e `18283B` em `126-20261118-0000`/`081_...` — todos em revisão.
- **ROMs com nomes similares mas datas diferentes** (ex.: `Super Mario World` U vs E) — terceiros, não mover.

> Para cada conjunto suspeito, nenhuma linha em `plano_movimentacao.csv` propõe mover para `D-Duplicados`; ação é `manter` com justificativa `REVISAO — nao mover`.

### 4.3 Pasta D-Duplicados — destino
```
Meu Drive/D-Duplicados/  (ID 1sC9IMFSDSLXF9roRqVhZd54gofXP2Q55 renomeado)
├─ 01-Odonto — TCLE e Contratos/
├─ 06-Pesquisa — Onlyoffice excedentes/
├─ 03-Cursos — Onlyoffice excedentes/
├─ 99.1 — Cópias excedentes/ (5 itens legado)
├─ Onlyoffice-26-11-02 — DUPLICADO/ (6 itens)
└─ _legado-tecnico/ (.DS_Store)
```
Ver `duplicatas.md` para árvore completa e justificativas por grupo.

---

## 5. Itens de terceiros / compartilhados — sinalizados, não alterados

| Local | Qtd | Detalhe | Ação proposta |
|---|---|---|---|
| `08 — Compartilhado` (shared=true) | 47 itens de `diogorego@gmail.com` | `OpenCode` 9 mp4, `ROM_SNES` 23 ROMs, `Maçonaria` 7 md + 2 png + 2 mp4 + 1 guia, 1 pasta `A Ordem e o Palco` (sua, compartilhada) | `nao alterar — item de terceiros` — mover somente com sua autorização explícita |
| `08 — Compartilhado` (seus, shared=true) | 30 itens | Módulos 01–09 (gslides) + roteiros .md + Ppt-A/B/C + 2 docx maçônicos + 1 smc Mario | `manter — compartilhado` — preservar permissões/links |
| Atalhos (10) | 10 | `Livros de Odontologia`, `Radiologia Oral Pharoah.pdf`, `Terapias Atuais`, `NETTER`, `Caminhos da Polpa`, `Cirurgia Buco Maxilo`, `Editais`, `ABO_Aperf-2026`, `Concursos`, `Cirurgia (atalho)` | `manter — atalho` — apontam para fora do seu Drive |
| Legado técnico | 3 | `.DS_Store` (×2) + `2026-11-03_DS_Store.bin` | `mover para D-Duplicados/_legado-tecnico` — arquivo de sistema |

Nenhuma permissão será alterada em qualquer fase.

---

## 6. Estado antes / depois (proposto, Fase 2)

| Métrica | Antes (atual, Fase 1) | Depois (proposto, Fase 2) | Delta |
|---|---|---|---|
| **Itens na raiz soltos** | 23 | 0 (movidos para `00 — Triagem` → destinos) | -23 |
| **Pastas na raiz** | 12 + `Aulas`/`comandos` | 12 + `Aulas`/`comandos` + `00 — Triagem` + `D-Duplicados` (renomeado de `99`) | +1 criada, 1 renomeada |
| **Itens em `D-Duplicados`** | 20 (em `99`) + 14 duplicatas confirmadas fora | 34 (20 já + 14 movidas) + 2 .DS_Store | +16 organizados |
| **Itens movidos** | 0 (DRY RUN) | 25 (23 raiz + 2 sistema) + 14 duplicatas = **39 movimentos** | — |
| **Itens renomeados (pasta)** | 0 | 1 (`99` → `D-Duplicados`, mesmo ID) | — |
| **Itens renomeados (arquivos)** | 0 | 0 na Fase 1; na Fase 2 `AAAA-MM-DD-*` somente quando data segura (ex.: `081_...` mantido) | — |
| **Não alterados** | 337 (todos) | 298 (manter + terceiros + atalhos + vazias) | — |
| **Erros** | 0 | 0 previstos — toda operação via `add_parents`+`remove_parents` preservando ID | — |

> **Relatório final pós-Fase 2** trará lista exata de `movidos`, `renomeados`, `organizados em D-Duplicados`, `não alterados` e `erros` com IDs.

---

## 7. Restrições obrigatórias — conformidade

- ✅ **Não excluir, não mover para lixeira, não substituir**: nenhum `delete_file`/`trash_file` chamado; Fase 1 só `list_files`/`get_file`.
- ✅ **Não alterar permissões/compartilhamentos**: `list_permissions` não usado para escrita; `shared=true` mantido.
- ✅ **Não modificar terceiros sem autorização**: 47 itens `diogorego` sinalizados, nenhuma ação proposta.
- ✅ **Preservar conteúdo e IDs**: todos os movimentos propostos são `update_file(add_parents, remove_parents)` — ID inalterado.
- ✅ **Se ação violar regra, não executar e explicar**: 10 grupos suspeitos com `REVISAO — nao mover` + justificativa.
- ✅ **Fase 2 só após aprovação explícita**: este relatório encerra Fase 1 e aguarda seu “OK”.

---

## 8. Entregáveis desta Fase 1 (neste workspace)

| Arquivo | O que é | Linhas |
|---|---|---|
| `inventario_completo.csv` | Inventário recursivo completo: `ID, nome, tipo, tamanho_bytes, localizacao_atual, data_modificacao, owner, compartilhado` | 338 (337 + cabeçalho) |
| `inventario_consolidado.py` | Mesmo inventário em Python (`ITEMS = [...]`) para reuso | — |
| `arvore_proposta.md` | Árvore de pastas proposta (00–09 + Aulas/comandos + D-Duplicados) | — |
| `plano_movimentacao.csv` | Plano de movimentação: `ID, nome, tipo, localização atual, localização proposta, ação, justificativa` | 338 |
| `duplicatas.csv` | 14 grupos confirmados — `manter (canônico)` vs `mover para D-Duplicados` | 29 |
| `duplicatas_revisao.csv` | 10 grupos suspeitos — `REVISAO — nao mover` | 24 |
| `duplicatas.md` | Lista legível das duplicatas com regras e destinos | — |
| `relatorio_fase1.md` | **Este relatório** — estado antes/depois + conformidade | — |

Todos em `/home/user/graphify/drive-fase1/` (workspace versionado no branch `arena/dc87a1d4-graphify`). Nenhum arquivo foi escrito no seu Drive.

---

## 9. Próximos passos — aguardando sua aprovação explícita

**NÃO iniciarei a Fase 2 sem seu OK por escrito neste chat.**

Quando você aprovar, executarei:

1. `create_file` para `00 — Triagem` e `D-Duplicados` + subpastas (se não existirem).
2. `update_file` renomeando `99 — Duplicados (nada foi apagado)` → `D-Duplicados`.
3. `update_file(add_parents, remove_parents)` para os 39 movimentos do `plano_movimentacao.csv` (23 raiz + 2 sistema + 14 duplicatas antigas).
4. Padronização de nomes `AAAA-MM-DD-*` somente onde data é segura; caso contrário manter e sinalizar.
5. Relatório final com antes/depois real + lista de erros (se houver).

**Responda:** `Aprovo Fase 1 e autorizo Fase 2 conforme plano` — ou indique ajustes (ex.: manter algum arquivo na raiz, não criar `00 — Triagem`, tratar `Aulas` diferente).

---

*Dúvidas sobre algum ID, duplicata ou atalho? Cite o `ID` ou `nome` que explico a justificativa linha a linha.*
