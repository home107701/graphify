# Árvore de Pastas Proposta — FASE 1 DRY RUN
*Google Drive de homebox765@gmail.com — varredura recursiva completa em 2026-11-21*
*337 itens verificados (pastas + arquivos) — nenhum item movido/criado/renomeado (somente leitura)*

## Princípios
- **Nenhuma exclusão**: todo ID preservado. `D-Duplicados` sucede `99 — Duplicados (nada foi apagado)` por renomeação/padronização.
- **Preservar compartilhamentos**: `08 — Compartilhado` permanece intacto (próprio compartilhado + terceiros sem autorização).
- **Atalhos não movidos**: 10 atalhos para pastas compartilhadas externas mantidos.
- **Mover só com segurança**: duplicatas só movidas quando mesmo nome normalizado + mesmo tamanho + data determinável; caso contrário → revisão.
- **Nomes padronizados na Fase 2**: `AAAA-MM-DD-Nome-assunto.ext` somente quando data segura; senão manter e sinalizar.

## Estrutura proposta (após aprovação)

```
Meu Drive/
│
├─ 00 — Triagem/                              [NOVO]  ← recebe 23 arquivos soltos na raiz
│   └─ (revisão inicial; esvaziado após mover para destinos finais)
│
├─ 01 — Odontologia e Saúde/                  [MANTER]
│   ├─ 01.1 — Documentos, TCLE e Contratos/   ← 14 TCLE/contratos já com prefixo AAAA-MM-DD
│   ├─ 01.2 — Guias, Farmacologia e Terapêutica/ ← 28 guias + protocolos
│   ├─ 01.3 — Aulas, Imaginologia e Mídia/   ← 10 arquivos + 15 que virão da raiz/Aulas
│   ├─ 01.4 — Livros, Tratados e Acervo/     ← vazio — manter reservado
│   ├─ 01.5 — Legado técnico (até 2018)/     ← 1 arquivo .DS_Store → mover para D-Duplicados/_legado-tecnico
│   ├─ RADIOLOGIA — Cirurgia Oral — Apresentações/ ← 14 apresentações (R001 + 00-08)
│   ├─ Sedação odontológica — 8 apresentações • Minimal Editorial Mono/ ← 9 itens
│   ├─ Medicamentos/                          ← 8 PDFs legados 2018
│   └─ Onlyoffice-P-Aulas-Odonto — MAIS RECENTE (mod. 2026-07-08)/ ← 3 subpastas vazias — manter p/ consolidação
│
├─ 02 — Jurídico/                             [MANTER]
│   ├─ 02.1 — Estudos, Minutas e IA Jurídica/ ← Manual Governança IA + Lex Clássico
│   ├─ Minuta — resolução contratual imobiliária/ ← 1 minuta
│   └─ Juspesq - Privado/                     ← 3 itens (PDR, zip, html)
│
├─ 03 — Cursos, Concursos e Editais/         [MANTER]
│   ├─ 03.1 — Editais, Grades e Material de Aula/ ← 7 PDFs (MAN-PED, HORÁRIO, GRA-*, etc)
│   ├─ Onlyoffice-Uninass — MAIS RECENTE (mod. 2026-06-26)/ ← PDFs2026 vazio — manter
│   └─ OL_2021-03/                             ← 2 .rar legados
│
├─ 04 — Biblioteca (Livros e PDFs)/           [MANTER]
│   ├─ 04.1 — Acervo Geral/                  ← vazio — manter
│   └─ Ebooks OL/                            ← 9 PDFs Medicina Legal 2018
│
├─ 05 — Apresentações/                        [MANTER]
│   └─ 05.1 — Slides e Imagens/              ← 11 itens (10 JPG 2026-11-08 + 1 gslides)
│
├─ 06 — Pesquisa, IA e Ferramentas/           [MANTER]
│   ├─ 06.1 — Documentos, Prompts e Roteiros/ ← 16 arquivos core (PFN, Site-IA, Prp-Aulas, etc) — CANÔNICO
│   ├─ 06.2 — Planilhas e Dados/              ← vazio — manter
│   ├─ Arena-transc/                          ← 15 itens Lotofácil/transc
│   ├─ Onlyoffice-2026-08 — MAIS RECENTE (mod. 2026-10-13)/ ← vazio pós-consolidação — manter temporariamente
│   ├─ Onlyoffice-Pesq-0001 — MAIS RECENTE (mod. 2026-06-25)/ ← 1 subpasta Cedula-Dolar vazia — manter
│   └─ 26-11_Arena — arquivo de trabalho (esvaziada)/ ← vazio — manter
│
├─ 07 — Arquivo Antigo/                       [MANTER]
│   └─ 07.1 — Legado e Versões Antigas/      ← 2 itens Mod07
│
├─ 08 — Compartilhado/                        [NÃO ALTERAR — compartilhado + terceiros]
│   ├─ Maçonaria/                             ← 14 itens (me: 2 docx + 1 md; diogorego: 7 md + 2 png + 2 mp4 + 1 guia)
│   │   └─ A Ordem e o Palco/                ← 2 arquivos (PPTX+PDF) — próprio, compartilhado
│   ├─ OpenCode/                              ← 9 mp4 de terceiros (diogorego) — NÃO MOVER
│   ├─ ROM_SNES/                              ← 23 ROMs de terceiros (diogorego) — NÃO MOVER
│   ├─ [14 próprios compartilhados na raiz de 08] Módulos 01-09 + roteiros + Ppt-A/B/C
│   └─ Super Mario World (U) [!].smc (meu)   ← duplicata de ROM — tratar como terceiro? manter
│
├─ 09 — OpenFree/                             [MANTER]
│   └─ 09.1 — Sites, Favoritos e Projetos/   ← 9 itens (favoritos, Luck, kit-memória)
│
├─ Aulas/                                     [MANTER TEMPORARIAMENTE]
│   └─ 7 itens cirurgia oral guiada — futura consolidação em 01.3 avaliada
│
├─ comandos/                                  [MANTER]
│   └─ Respostas anteriores — comandos e relatório do Drive (1 gdoc)
│
└─ D-Duplicados/                              [NOVO — sucede 99 por renomeação, preserva ID 1sC9IMF...]
    ├─ 01-Odonto — TCLE e Contratos excedentes/  ← TCLE-Tracionamento, TCLE-Exod-Protocolo, Contratos
    ├─ 06-Pesquisa — Onlyoffice excedentes/      ← Obsidian, PFN, Pesquisa_Automot, Prp-Aulas, V2-Prpt, Sites-IA
    ├─ 03-Cursos — Onlyoffice excedentes/        ← MAN-PED, HORÁRIO, GRA-MAT/PLE
    ├─ 99.1 — Cópias excedentes/                 ← 5 itens já isolados (legado)
    ├─ Onlyoffice-26-11-02 — DUPLICADO/         ← 6 itens (4 cópias Onlyoffice + .DS_Store + NotebookLM)
    │   ├─ Onlyoffice-2026-08 — cópia/
    │   ├─ Onlyoffice-Uninass — cópia/PDFs2026/
    │   ├─ Onlyoffice-Pesq-0001 — cópia/Cedula-Dolar/
    │   └─ Onlyoffice-P-Aulas-Odonto — cópia/
    └─ _legado-tecnico/                         ← .DS_Store, 2026-11-03_DS_Store.bin
```

## O que muda na Fase 2 (após aprovação)
- **Criar** `00 — Triagem` e `D-Duplicados` (+ subpastas temáticas).
- **Renomear** `99 — Duplicados (nada foi apagado)` → `D-Duplicados` (preserva ID `1sC9IMF...`).
- **Mover 23 arquivos soltos na raiz** para `00 — Triagem` e de lá para destinos finais (01.3, 04.1, 06.1) — ver `plano_movimentacao.csv` ação `mover`.
- **Mover 2 arquivos de sistema** para `D-Duplicados/_legado-tecnico`.
- **Mover somente duplicatas antigas** (14 grupos confirmados) para `D-Duplicados` em subpastas; manter a mais recente na árvore.
- **Não mover**: 47 itens de terceiros, 30 próprios compartilhados, 10 atalhos, pastas vazias estruturais.
- **Renomear na Fase 2**: `AAAA-MM-DD-Nome-assunto.ext` somente quando data segura; senão manter e sinalizar (ex.: `081_2026-11-18_0043` sem data confiável).

## Pastas vazias — decisão
Manter vazias: `01.4`, `04.1`, `06.2`, `26-11_Arena`, `PDFs2026`, `Cedula-Dolar` (estrutura Onlyoffice em consolidação). Reavaliar após Fase 2.

## Itens de terceiros/compartilhados — sinalizados
- Toda `08 — Compartilhado` (owner diogorego: OpenCode 9 mp4, ROM_SNES 23 ROMs, 7 md + 2 png + 2 mp4 em Maçonaria) → `nao alterar — item de terceiros`.
- Módulos 01–09 próprios em `08` compartilhados com terceiros → `manter — compartilhado` (preserva links).
- Atalhos (Livros, Radiologia Oral, Terapias Atuais, NETTER, Caminhos da Polpa, Cirurgia, Editais, ABO_Aperf-2026, Concursos) → `manter — atalho`.
