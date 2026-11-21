# -*- coding: utf-8 -*-
import csv, os, pathlib

ROOT = pathlib.Path("/home/user/graphify/drive-fase1")
# Load existing dados
ITEMS = []
exec(open(ROOT/"dados1.py").read())
exec(open(ROOT/"dados2.py").read())
exec(open(ROOT/"dados3.py").read())
exec(open(ROOT/"dados4.py").read())

# Add missing items fetched in second sweep (manual append from outputs)
# 01 root subfolders already in dados2? Actually 16Zvt children were fetched now - but dados didn't have them earlier? Let's add them as ITEMS if not present.
# Instead we will append all recently fetched items (we have IDs, ensure no duplicate)
recent = [
# From 16Zvt (01 Odontologia root)
("1wQLPZ1MDPkJwkdg0HB42LbmQnLa-p19N","RADIOLOGIA — Cirurgia Oral — Apresentações","folder","","2026-11-17T09:46:58Z","Meu Drive/01 — Odontologia e Saúde","me",False),
("1ktRa2YtfW7wKk_BwGrsIBVpRlCKu6bS9","01.5 — Legado técnico (até 2018)","folder","","2026-11-11T19:20:18Z","Meu Drive/01 — Odontologia e Saúde","me",False),
("1Ip55AjQuBv600OcAKBkiogDNnQkEKuEQ","01.4 — Livros, Tratados e Acervo","folder","","2026-11-11T19:20:16Z","Meu Drive/01 — Odontologia e Saúde","me",False),
("179bkjoVvIfpDaxbEbFZNVrPmtni2KeaY","01.3 — Aulas, Imaginologia e Mídia","folder","","2026-11-11T19:20:15Z","Meu Drive/01 — Odontologia e Saúde","me",False),
("1QtiY4z_W-VMJPXkKFuIuAiiS7YwohUCO","01.2 — Guias, Farmacologia e Terapêutica","folder","","2026-11-11T19:20:13Z","Meu Drive/01 — Odontologia e Saúde","me",False),
("1iVriEvazZMe2Mylsc_vdE4g3eh7UQZcM","01.1 — Documentos, TCLE e Contratos","folder","","2026-11-11T19:20:06Z","Meu Drive/01 — Odontologia e Saúde","me",False),
("1D1jg6LbAbe1YyEA-_7jBaYQIDI_BVYCx","Cirurgia (atalho — pasta compartilhada)","shortcut","","2026-11-09T20:40:21Z","Meu Drive/01 — Odontologia e Saúde","me",False),
("1Jt90qvyPpG3ch_Jlfi3zz9KMYaUNmfik","Onlyoffice-P-Aulas-Odonto — MAIS RECENTE (mod. 2026-07-08)","folder","","2026-11-09T20:38:57Z","Meu Drive/01 — Odontologia e Saúde","me",False),
("1OeegoAlp6uJl9RB6DQWFGnTGWRKNROOX","Sedação odontológica — 8 apresentações • Minimal Editorial Mono","folder","","2026-11-09T12:28:02Z","Meu Drive/01 — Odontologia e Saúde","me",False),
("1xZUh2BofloLJGa48VR8IbNqr8y7JXYrV","Medicamentos","folder","","2018-06-06T15:17:46Z","Meu Drive/01 — Odontologia e Saúde","me",False),
# 09
("105GJ2ou0slVHP3X5KYHCoMidVSVHMm6W","09.1 — Sites, Favoritos e Projetos","folder","","2026-11-11T19:20:46Z","Meu Drive/09 — OpenFree","me",False),
# 99
("1wxbvotV8Kh50WF47qAJqwQsgMJ7QTiC1","99.1 — Cópias excedentes","folder","","2026-11-11T19:20:48Z","Meu Drive/99 — Duplicados (nada foi apagado)","me",False),
("1-dXLUoatO2pnrGAM3opHEUau0miU466o","Onlyoffice-26-11-02 — DUPLICADO (cópia de 26-11_Arena; mod. mais recente 2026-10-13)","folder","","2026-11-09T20:40:44Z","Meu Drive/99 — Duplicados (nada foi apagado)","me",False),
# RADIOLOGIA contents (14)
("1NYjKgrbkFJtTRBlnB6YdU8q4kTEX00StryBwP2At1ew","R001_20-11-26_1154 — roteiro de produção (20 slides)","gdoc","17582","2026-11-20T11:54:11Z","Meu Drive/01 — Odontologia e Saúde/RADIOLOGIA — Cirurgia Oral — Apresentações","me",False),
("16P2QVGiQSwZPrLTvmOska5L2bkwh9HDXpxTxC-6AKzw","R001_20-11-26_1154","gslides","691254","2026-11-20T11:54:11Z","Meu Drive/01 — Odontologia e Saúde/RADIOLOGIA — Cirurgia Oral — Apresentações","me",False),
("1yunnwxlq4G1or9YoffeMSgYzFP0X8Owz","R001_20-11-26_1154 (PDF para projeção).pdf","pdf","889040","2026-11-20T11:54:10Z","Meu Drive/01 — Odontologia e Saúde/RADIOLOGIA — Cirurgia Oral — Apresentações","me",False),
("1WfToJh6wT2sowJN-wPmB2UCDYgxvKJTS","Radiologia e Tomografia em Terceiros Molares — 40 slides (PDF para projeção).pdf","pdf","4735485","2026-11-20T10:08:43Z","Meu Drive/01 — Odontologia e Saúde/RADIOLOGIA — Cirurgia Oral — Apresentações","me",False),
("1FkrqM7AKq6xGB84Tc2pTGyRrzE7bZDvY1CdakvFM1kk","Roteiro de Direção de Arte — Radiologia e Tomografia em Terceiros Molares (40 slides)","gdoc","27419","2026-11-20T10:07:16Z","Meu Drive/01 — Odontologia e Saúde/RADIOLOGIA — Cirurgia Oral — Apresentações","me",False),
("1YazsYZscDb4jzmxCDPFfRZoWL0fZvjNHA4NeATkJ57M","04 — RADIOLOGIA — Patologias que Mudam a Conduta — 15 slides","gslides","166949","2026-11-17T09:47:08Z","Meu Drive/01 — Odontologia e Saúde/RADIOLOGIA — Cirurgia Oral — Apresentações","me",False),
("1V1-lrvbq46xAH3qbqLe9W8vFZB9InHvl4pwW8MY5Fg0","05 — RADIOLOGIA — DTM, RM e Ultrassonografia — 15 slides","gslides","152860","2026-11-17T09:47:08Z","Meu Drive/01 — Odontologia e Saúde/RADIOLOGIA — Cirurgia Oral — Apresentações","me",False),
("1M4cH6Ifq0WYzOWI_m6CSt4sLcIB-lN-ZbR-_4o6SPIo","07 — RADIOLOGIA — Síntese e Avaliação — 15 slides","gslides","122998","2026-11-17T09:47:08Z","Meu Drive/01 — Odontologia e Saúde/RADIOLOGIA — Cirurgia Oral — Apresentações","me",False),
("1VkADbpT2t6HAKQ3rQ70poWv-8ML_qmjRsrxjjg8rRsk","08 — RADIOLOGIA — 100 SLIDES — Apresentação Completa","gslides","766860","2026-11-17T09:47:08Z","Meu Drive/01 — Odontologia e Saúde/RADIOLOGIA — Cirurgia Oral — Apresentações","me",False),
("1gf_70_RVeSQq0dOMr8W7XWymVvT80iCuoNQgZqZDpO8","06 — RADIOLOGIA — Oficina Integradora — 15 slides","gslides","174466","2026-11-17T09:47:08Z","Meu Drive/01 — Odontologia e Saúde/RADIOLOGIA — Cirurgia Oral — Apresentações","me",False),
("1osJvb0XcW8S1sVtO6ER9LcVpbn5S8KIbikHnrZJuiAU","02 — RADIOLOGIA — Radiografia e TCFC — 15 slides","gslides","141571","2026-11-17T09:46:58Z","Meu Drive/01 — Odontologia e Saúde/RADIOLOGIA — Cirurgia Oral — Apresentações","me",False),
("1RKh_is3502pNHUMZEtwudHuJ2KLxY8lvF8GgqOL3rNM","00 — RADIOLOGIA — Aula Completa — 56 slides","gslides","103492","2026-11-17T09:46:58Z","Meu Drive/01 — Odontologia e Saúde/RADIOLOGIA — Cirurgia Oral — Apresentações","me",False),
("1t5W9919DZx-eqL6QLb1x0R0EEIiNjr74taC0g8J79dw","03 — RADIOLOGIA — Terceiros Molares: Planejamento — 15 slides","gslides","182104","2026-11-17T09:46:58Z","Meu Drive/01 — Odontologia e Saúde/RADIOLOGIA — Cirurgia Oral — Apresentações","me",False),
("1OPJ0pKNzs_9-G6bIyVhBlwH1sr4pfaK6HH8N2mDkInw","01 — RADIOLOGIA — Abertura: Da imagem à decisão — 15 slides","gslides","139270","2026-11-17T09:46:58Z","Meu Drive/01 — Odontologia e Saúde/RADIOLOGIA — Cirurgia Oral — Apresentações","me",False),
# 01.1 etc - sample, we already have them via earlier fetch but we add full lists from outputs
("18HdT4JZ4LJr3mutGmSIVH9gDowlT_goI","2026-11-09_TCLE-Tracionamento_MAIS_RECENTE.docx","docx","23025","2026-11-11T19:27:00Z","Meu Drive/01 — Odontologia e Saúde/01.1 — Documentos, TCLE e Contratos","me",False),
("1ENNOhTsvXijHsxaN0nxlr-8KxxRXoa--","2026-07-08_TCLE-Exodontia.docx","docx","25251","2026-11-11T19:26:58Z","Meu Drive/01 — Odontologia e Saúde/01.1 — Documentos, TCLE e Contratos","me",False),
("18eDCIr4W1tg9w7DETpblMyS7FQl5EYb_","2026-07-08_TCLE-Exod-Protocolo.docx","docx","24922","2026-11-11T19:26:56Z","Meu Drive/01 — Odontologia e Saúde/01.1 — Documentos, TCLE e Contratos","me",False),
("1yvTpvfBqzc8xiHRmQcD79vtwAyDJIkQ5","2026-07-08_TCLE-Exod-Protocolo-26-7.docx","docx","25037","2026-11-11T19:26:55Z","Meu Drive/01 — Odontologia e Saúde/01.1 — Documentos, TCLE e Contratos","me",False),
("17oKt7BibRlzynKCawcf4z8Yd0wrwFecp","2026-11-09_TCLE-Exod-Protocolo_MAIS_RECENTE.pdf","pdf","91221","2026-11-11T19:26:54Z","Meu Drive/01 — Odontologia e Saúde/01.1 — Documentos, TCLE e Contratos","me",False),
("1OYtNy36aU8yWgwFYOtwzHpSNLtNcvChc","2026-07-08_TCLE-Contrato-Ortodontia.docx","docx","22720","2026-11-11T19:26:52Z","Meu Drive/01 — Odontologia e Saúde/01.1 — Documentos, TCLE e Contratos","me",False),
("1sYN-1FcIkULOnWzFuOAt4j7HAeJSoabf","2026-07-08_TCLE-Contrato-Implante.pdf","pdf","90943","2026-11-11T19:26:50Z","Meu Drive/01 — Odontologia e Saúde/01.1 — Documentos, TCLE e Contratos","me",False),
("1pC2D33euRV1oBcoopcGBaJFPxgCoDEso","2026-07-08_TCLE_-_HAPVIDA_Cir_Invasiva.docx","docx","57787","2026-11-11T19:26:49Z","Meu Drive/01 — Odontologia e Saúde/01.1 — Documentos, TCLE e Contratos","me",False),
("1OOx3fHUdQuYBlmbLMhx8tKyJO0lFtq_Y","2026-06-25_Processos-Odonto-CFO-CFM.docx","docx","37793","2026-11-11T19:26:26Z","Meu Drive/01 — Odontologia e Saúde/01.1 — Documentos, TCLE e Contratos","me",False),
("1Dk_FPTifh7Hcox5qlB605C8NdWdRjhUW","2026-07-08_MT-CONTRATO_MS_CLINICA_MELHORADO.docx","docx","25370","2026-11-11T19:25:47Z","Meu Drive/01 — Odontologia e Saúde/01.1 — Documentos, TCLE e Contratos","me",False),
("12gI-aU3XJFSWKIYda-HWvaUfu2FRfE7s","2026-07-08_MARCELLO-TCLE_e_Contrato_Odontologico.docx","docx","41886","2026-11-11T19:25:42Z","Meu Drive/01 — Odontologia e Saúde/01.1 — Documentos, TCLE e Contratos","me",False),
("1Mh_c29V6kIWpB0KAI7Jxg4UNJKHd4J4O","2026-06-25_Evolucao-Prontuario-Modelo.docx","docx","1070640","2026-11-11T19:24:44Z","Meu Drive/01 — Odontologia e Saúde/01.1 — Documentos, TCLE e Contratos","me",False),
("13stdrP-jicEVG9PZDFun1iEIO2mVB1gC","2026-11-09_Contrato_Implante_MS_LGPD_CRO_20_paginas_carimbo_menor_linha_livre.pdf","pdf","3896722","2026-11-11T19:23:56Z","Meu Drive/01 — Odontologia e Saúde/01.1 — Documentos, TCLE e Contratos","me",False),
("1USW8FJXJ2E1Qa5E34MD8pQTqyPeWUN9B","2026-11-09_CONTRATO_DE_PRESTAÇÃO_DE_SERVIÇOS_PROFISSIONAIS.docx","docx","42105","2026-11-11T19:23:53Z","Meu Drive/01 — Odontologia e Saúde/01.1 — Documentos, TCLE e Contratos","me",False),
# 01.2
("11li2dF8PgNfLQW5ADQhh2hCb8gnnIPOi","2026-06-25_Visualização_Digital_e_Inovação_na_Cirurgia_Bucomaxilofacial.docx","docx","8645","2026-11-11T19:27:06Z","Meu Drive/01 — Odontologia e Saúde/01.2 — Guias, Farmacologia e Terapêutica","me",False),
("1vCZ5FcHF87aYOlOVSaMifq3Oc1rBa39o","2026-06-25_Uso_de_Opioides_na_Prática_Odontológica_Contemporânea.docx","docx","9035","2026-11-11T19:27:03Z","Meu Drive/01 — Odontologia e Saúde/01.2 — Guias, Farmacologia e Terapêutica","me",False),
("1rMPExJMP1auYwcR065c37HHNh5-0qlI9","2026-06-25_Protocolo_e_Manejo_das_Dores_Orofaciais_no_SUS.docx","docx","9082","2026-11-11T19:26:30Z","Meu Drive/01 — Odontologia e Saúde/01.2 — Guias, Farmacologia e Terapêutica","me",False),
("1q2Ax2EafCVb5BHxEDkyPZr-c_1tMIIlg","2026-07-08_Prompts_para_Orientação_Crítica_de_TCC.docx","docx","3326293","2026-11-11T19:26:28Z","Meu Drive/01 — Odontologia e Saúde/01.2 — Guias, Farmacologia e Terapêutica","me",False),
("1c5pmPZqZE1fE5fWHUWZji37WQF5paM2w","2026-06-25_Manejo_Farmacológico_em_Pacientes_com_Necessidades_Especiais.docx","docx","9083","2026-11-11T19:25:29Z","Meu Drive/01 — Odontologia e Saúde/01.2 — Guias, Farmacologia e Terapêutica","me",False),
("1y_yE68EOFsy7rVGDIpHdp1wl0Aj--cNP","2026-06-25_Manejo_Farmacológico_da_Dor_e_Inflamação_em_Pediatria.docx","docx","9126","2026-11-11T19:25:28Z","Meu Drive/01 — Odontologia e Saúde/01.2 — Guias, Farmacologia e Terapêutica","me",False),
("1_TRWdePiaXtmcb5YRwsxDOyQ-rmwpvof","2026-06-25_Manejo_da_Dor_e_Inflamação_na_Prática_Odontológica.docx","docx","8917","2026-11-11T19:25:26Z","Meu Drive/01 — Odontologia e Saúde/01.2 — Guias, Farmacologia e Terapêutica","me",False),
("1DtD8HiNhGqXxmk_WozTcBlLZ8XOZHbgs","2026-06-25_GuiaTerapeuticoOdontologia.pdf","pdf","2755668","2026-11-11T19:25:11Z","Meu Drive/01 — Odontologia e Saúde/01.2 — Guias, Farmacologia e Terapêutica","me",False),
("18jfqOeXmo9KmMjKffJfmgKyGGC-gN6ZJ","2026-06-25_Guia_Prático_de_Terapêutica_Odontológica_no_SUS.docx","docx","7180","2026-11-11T19:25:02Z","Meu Drive/01 — Odontologia e Saúde/01.2 — Guias, Farmacologia e Terapêutica","me",False),
("1iLNFDhhnb8_4akfgFyYxz7eTvGz-ixsT","2026-06-25_Guia_de_Estudos_Distinção_Jurídica_entre_Mero_Aborrecimento_e_Dano_Moral.docx","docx","10732","2026-11-11T19:25:00Z","Meu Drive/01 — Odontologia e Saúde/01.2 — Guias, Farmacologia e Terapêutica","me",False),
("1_hhZ43680-IMhKTT_72Ov1TrM-6GIPUo","2026-06-25_Guia_Completo_de_Anestésicos_Locais_e_Prática_Odontológica.docx","docx","9008","2026-11-11T19:24:58Z","Meu Drive/01 — Odontologia e Saúde/01.2 — Guias, Farmacologia e Terapêutica","me",False),
("1RQtn8dHvrmCYDlJ6LboJR1IU_4LXHBIV","2026-06-25_Fundamentos_Fisiopatológicos_da_Dor_e_Inflamação_Orofacial.docx","docx","9075","2026-11-11T19:24:50Z","Meu Drive/01 — Odontologia e Saúde/01.2 — Guias, Farmacologia e Terapêutica","me",False),
("1caiqY8Cfc3ipsUAbG4myo0OVQrf6xAGm","2026-06-25_Fisiopatologia_da_Dor_na_Odontologia.png","png","4593833","2026-11-11T19:24:47Z","Meu Drive/01 — Odontologia e Saúde/01.2 — Guias, Farmacologia e Terapêutica","me",False),
("18RVhM6nPeMyUIv57CNxZaiqz6W6O2-f8","2026-06-25_Essential_Dental_Prescribing.pptx","pptx","14591086","2026-11-11T19:24:41Z","Meu Drive/01 — Odontologia e Saúde/01.2 — Guias, Farmacologia e Terapêutica","me",False),
("1ykMa6wgP3t7_DteuyEF630az6_Tm4B7J","2026-06-25_Distinção_Jurídica_entre_Mero_Aborrecimento_e_Dano_Moral_Guia_de_Estudos_Completo.docx","docx","12290","2026-11-11T19:24:25Z","Meu Drive/01 — Odontologia e Saúde/01.2 — Guias, Farmacologia e Terapêutica","me",False),
("1YzE20GeV0VI1Cg-ZVeU6FZP7mNVvo-tf","2026-06-25_Diretrizes_para_Prescrição_Odontológica_e_Controle_de_Medicamentos.docx","docx","8757","2026-11-11T19:24:24Z","Meu Drive/01 — Odontologia e Saúde/01.2 — Guias, Farmacologia e Terapêutica","me",False),
("1sWeo8EPkmCDdP6ksSSDUKk5z2un74k7X","2026-06-25_Diretrizes_para_o_Uso_de_Corticosteroides_na_Odontologia.docx","docx","8948","2026-11-11T19:24:22Z","Meu Drive/01 — Odontologia e Saúde/01.2 — Guias, Farmacologia e Terapêutica","me",False),
("1nBPIjA0TiL7cnFB6pVaha3pcpOv38WsF","2026-06-25_Cannabis_na_Dor_Orofacial.pptx","pptx","13143720","2026-11-11T19:23:51Z","Meu Drive/01 — Odontologia e Saúde/01.2 — Guias, Farmacologia e Terapêutica","me",False),
("1Q0CZM1mujarW34V_edw9_vDUGllt0nIo","2026-06-25_Cannabis_Medicinal_no_Tratamento_da_Dor_Orofacial_e_Odontologia.docx","docx","9239","2026-11-11T19:23:50Z","Meu Drive/01 — Odontologia e Saúde/01.2 — Guias, Farmacologia e Terapêutica","me",False),
("1KFG04fWhs6XGjXKMkEG49kcETd8Nku_0","2026-06-25_Cannabis_Medicinal_no_Manejo_da_Dor_Orofacial_e_Odontologia.docx","docx","9239","2026-11-11T19:23:48Z","Meu Drive/01 — Odontologia e Saúde/01.2 — Guias, Farmacologia e Terapêutica","me",False),
("1KsWyUTiNVfCDCJCZjizPDde70fxOT6TH","2026-07-08_Antonio-Pcte-Duilyo-2.pdf","pdf","108140","2026-11-11T19:23:17Z","Meu Drive/01 — Odontologia e Saúde/01.2 — Guias, Farmacologia e Terapêutica","me",False),
("1VnK5Ji9KAGHcnSX4V2fGfF5BahU9eFdk","2026-06-25_81-120.docx","docx","18520","2026-11-11T19:23:11Z","Meu Drive/01 — Odontologia e Saúde/01.2 — Guias, Farmacologia e Terapêutica","me",False),
("1l2kCU-sBBOJH3EZAWXG9hMRXlPPTrK0s","2026-06-25_41-80.docx","docx","18721","2026-11-11T19:23:09Z","Meu Drive/01 — Odontologia e Saúde/01.2 — Guias, Farmacologia e Terapêutica","me",False),
("1IpCcaVnONSybk4AgPdIeo-y0Ny6RHKoW","2026-06-25_241-280.docx","docx","17879","2026-11-11T19:23:08Z","Meu Drive/01 — Odontologia e Saúde/01.2 — Guias, Farmacologia e Terapêutica","me",False),
("1VWh45ZkLJ33xTIKT6_4pQPv9MW2dUg5R","2026-06-25_201-240.docx","docx","18760","2026-11-11T19:23:04Z","Meu Drive/01 — Odontologia e Saúde/01.2 — Guias, Farmacologia e Terapêutica","me",False),
("1XTKPSIQB5rHWKNNxmMeelFN_TrF7yDuI","2026-06-25_161-200.docx","docx","20479","2026-11-11T19:22:49Z","Meu Drive/01 — Odontologia e Saúde/01.2 — Guias, Farmacologia e Terapêutica","me",False),
("10JAY8n2t6swqJ6Y3PpC0HxpOUYGZ40ne","2026-06-25_121-160.docx","docx","19392","2026-11-11T19:22:48Z","Meu Drive/01 — Odontologia e Saúde/01.2 — Guias, Farmacologia e Terapêutica","me",False),
("1SGipqLovlEHdfnWNsF0hGKNvCwacpuPK","2026-06-25_1-40.docx","docx","18565","2026-11-11T19:22:46Z","Meu Drive/01 — Odontologia e Saúde/01.2 — Guias, Farmacologia e Terapêutica","me",False),
# 01.3
("1D3qAgHWMhsskkQdyDT58xRZ5xHZaHzKA","2026-06-25_Special_Patient_Clinical_Dashboard.pptx","pptx","16548412","2026-11-11T19:26:48Z","Meu Drive/01 — Odontologia e Saúde/01.3 — Aulas, Imaginologia e Mídia","me",False),
("1-F04K0RNwjovXKM_f-3LpLIczBpa3SPy","2026-06-25_Revolução_3D_na_Bucomaxilo.mp4","mp4","46461560","2026-11-11T19:26:37Z","Meu Drive/01 — Odontologia e Saúde/01.3 — Aulas, Imaginologia e Mídia","me",False),
("1Cp-Ec-JPAl3zLXt6BL7AS0iz5GvEwuVv","2026-06-25_Resumo.docx","docx","7195","2026-11-11T19:26:36Z","Meu Drive/01 — Odontologia e Saúde/01.3 — Aulas, Imaginologia e Mídia","me",False),
("1Uvf_KZmD0jtrAhPErcNWwo1SCas80F-A","2026-06-25_PNE_Clinical_Control_Panel.pptx","pptx","24125785","2026-11-11T19:26:24Z","Meu Drive/01 — Odontologia e Saúde/01.3 — Aulas, Imaginologia e Mídia","me",False),
("1ISBVjR_y2HfyZDwiUH0-5yrx4VClNJGH","2026-06-25_plano-aula.docx","docx","10944","2026-11-11T19:26:23Z","Meu Drive/01 — Odontologia e Saúde/01.3 — Aulas, Imaginologia e Mídia","me",False),
("14X_cKgkF6UodQj1Kcy1owtlfs90K7i-o","2026-06-25_Plano_de_Aula_e_Roteiro_Imaginologia_em_CTBMF.docx","docx","3217177","2026-11-11T19:26:22Z","Meu Drive/01 — Odontologia e Saúde/01.3 — Aulas, Imaginologia e Mídia","me",False),
("10LhtXdQqdJ17YQmj1ar8cE98ifMLexj6","2026-06-25_Modern_Maxillofacial_Surgical_Navigation.pptx","pptx","19679170","2026-11-11T19:25:45Z","Meu Drive/01 — Odontologia e Saúde/01.3 — Aulas, Imaginologia e Mídia","me",False),
("1A0oSKgHWcORfC0JqKQ3XjGITuCfLyEvJ","2026-06-25_Imaginologia_Avançada_na_CTBMF.png","png","5065499","2026-11-11T19:25:15Z","Meu Drive/01 — Odontologia e Saúde/01.3 — Aulas, Imaginologia e Mídia","me",False),
("1rEGm0PqOnT34rqw8r60zQWX6OazX0Km9","2026-06-25_Digital_Surgical_Blueprint.pptx","pptx","29469229","2026-11-11T19:24:02Z","Meu Drive/01 — Odontologia e Saúde/01.3 — Aulas, Imaginologia e Mídia","me",False),
("1fGfdBoRWtcxXxcnyqIjnHizx4GLjrlib","2026-06-25_Digital_Maxillofacial_Ecosystem.pptx","pptx","15673595","2026-11-11T19:24:00Z","Meu Drive/01 — Odontologia e Saúde/01.3 — Aulas, Imaginologia e Mídia","me",False),
# 01.5
("1UxDE6X0W6oyXkUK3bYDl9zGx90avZ0A6","2026-11-03_DS_Store.bin","bin","10244","2026-11-11T19:21:40Z","Meu Drive/01 — Odontologia e Saúde/01.5 — Legado técnico (até 2018)","me",False),
# Sedação
("1QlGypBXj5Eu5EubWR32xYYB2RPCEEMni","2026-11-09_Roteiro_completo_120_slides_fontes_e_prompts.md","md","323186","2026-11-11T19:26:46Z","Meu Drive/01 — Odontologia e Saúde/Sedação odontológica — 8 apresentações • Minimal Editorial Mono","me",False),
("1SYlvjkeUhKz3zBmb7hTRw9Y4QTX1gfQ6yrAbzdJ6Gnk","2026-11-09_08_Cenário_judicial_e_implantação_Sedação_odontológica.gslides","gslides","517045","2026-11-11T19:22:44Z","Meu Drive/01 — Odontologia e Saúde/Sedação odontológica — 8 apresentações • Minimal Editorial Mono","me",False),
("1fIEJEEeZwfoHrr0wdCyurgRd2QCNbUTzDNVVIe7ee3I","2026-11-09_07_Ética_documentos_e_medicamentos_Sedação_odontológica.gslides","gslides","511547","2026-11-11T19:22:43Z","Meu Drive/01 — Odontologia e Saúde/Sedação odontológica — 8 apresentações • Minimal Editorial Mono","me",False),
("1OFOyEazuKR5nEhrNsEqZ8zH9CLuXFTp4eZQ0UWZyvwA","2026-11-09_06_Infraestrutura_e_norma_médica_Sedação_odontológica.gslides","gslides","494386","2026-11-11T19:22:40Z","Meu Drive/01 — Odontologia e Saúde/Sedação odontológica — 8 apresentações • Minimal Editorial Mono","me",False),
("1ntK7XmYxr02DGmHy91GYaCMZNdhwdrG6h2hP60xEO0E","2026-11-09_05_O_N_O_e_saúde_ocupacional_Sedação_odontológica.gslides","gslides","447911","2026-11-11T19:22:38Z","Meu Drive/01 — Odontologia e Saúde/Sedação odontológica — 8 apresentações • Minimal Editorial Mono","me",False),
("1MGXTFO3KYkwiHuYDCyRB9zcd44S06aRlKZSRy7t86y0","2026-11-09_04_CFO_295_e_habilitação_Sedação_odontológica.gslides","gslides","510961","2026-11-11T19:22:36Z","Meu Drive/01 — Odontologia e Saúde/Sedação odontológica — 8 apresentações • Minimal Editorial Mono","me",False),
("1aI1ps5ab-ngPdpztR4vpXyWYy1qk7BxrqQGNDqH2a9A","2026-11-09_03_Base_legal_e_CFM_×_CFO_Sedação_odontológica.gslides","gslides","517363","2026-11-11T19:22:34Z","Meu Drive/01 — Odontologia e Saúde/Sedação odontológica — 8 apresentações • Minimal Editorial Mono","me",False),
("1A_qMXfX7K6I92qwx_ebu_Sre6sdBEnCSDBwE5ESqSsQ","2026-11-09_02_Níveis_de_sedação_Sedação_odontológica.gslides","gslides","523565","2026-11-11T19:22:31Z","Meu Drive/01 — Odontologia e Saúde/Sedação odontológica — 8 apresentações • Minimal Editorial Mono","me",False),
("1NiGU0fZAZYgfGJAEjdY88JPI1Xf1mK4SzNGNCHBdK_o","2026-11-09_01_Síntese_executiva_Sedação_odontológica.gslides","gslides","486920","2026-11-11T19:22:29Z","Meu Drive/01 — Odontologia e Saúde/Sedação odontológica — 8 apresentações • Minimal Editorial Mono","me",False),
# Medicamentos
("1FxRAEo5T-nfwWLdDZWKMvXWXC8k0X1tx","2018-06-06_PROTOCOLOS_PARA_IMPLANTODONTIA.doc","doc","80896","2026-11-11T19:26:32Z","Meu Drive/01 — Odontologia e Saúde/Medicamentos","me",False),
("1e6ZOP0gd2JvJMsNlnQfB2maHY6ZAQC7S","2018-06-06_Protocolos_Farmacológicos_CTBMF_HU-UFPI_2015.pdf","pdf","503651","2026-11-11T19:26:31Z","Meu Drive/01 — Odontologia e Saúde/Medicamentos","me",False),
("1Reu3hivgi3XMiI-D8f-l4kockEVZiDKQ","2018-06-06_Portaria_344_98.pdf","pdf","117485","2026-11-11T19:26:25Z","Meu Drive/01 — Odontologia e Saúde/Medicamentos","me",False),
("1LAxpCVZQUAtsU0Ry3MS9WzI1YmPycwv7","2018-06-06_Medicamentos_-_source.pdf","pdf","229081","2026-11-11T19:25:42Z","Meu Drive/01 — Odontologia e Saúde/Medicamentos","me",False),
("1oxjtzscFeKYUI7-Z5fvwbsHQrRUAc2JN","2018-06-06_Guia_Genericos.pdf","pdf","870457","2026-11-11T19:25:10Z","Meu Drive/01 — Odontologia e Saúde/Medicamentos","me",False),
("1FlHTqF-FppJnIxKz_u1XGk808Gk1A-GX","2018-06-06_Doses_de_Medicamentos_mais_usados_em_Pediatria.pdf","pdf","283538","2026-11-11T19:24:27Z","Meu Drive/01 — Odontologia e Saúde/Medicamentos","me",False),
("1lZ_5A6sVW3_lockHuwr9rRWJ2svxT2IL","2018-06-06_Aula_Terapeutica_Meeting_Santos_Implante-2009.pdf","pdf","3452537","2026-11-11T19:23:23Z","Meu Drive/01 — Odontologia e Saúde/Medicamentos","me",False),
("10_uAdm5rXR4iey4GQb-OSHRVjzWHAcqP","2018-06-06_Antibioticoterapia_CCIH_-_PI.pdf","pdf","398431","2026-11-11T19:23:16Z","Meu Drive/01 — Odontologia e Saúde/Medicamentos","me",False),
# 09.1
("1LI7P8Qu2ZzZQckclDkqQvKQBehvK-hw9","favoritos-unificados-2026-11-13.zip","zip","879008","2026-11-14T00:20:31Z","Meu Drive/09 — OpenFree/09.1 — Sites, Favoritos e Projetos","me",False),
("1lhuTiZ7KB4FCOOUv6jPEVSt4T_4G04v0xIoaubWEW9c","2026-11-10_O_Conjunto_Recomendado_guia_didático.gdoc","gdoc","8984","2026-11-11T19:25:49Z","Meu Drive/09 — OpenFree/09.1 — Sites, Favoritos e Projetos","me",False),
("199lWcTUrFLYJCQE3WoNc2RQjOalklYH67tuDmcD3s28","2026-11-10_Luck_Jogos_e_Dados.gsheet","gsheet","3080","2026-11-11T19:25:24Z","Meu Drive/09 — OpenFree/09.1 — Sites, Favoritos e Projetos","me",False),
("127WUyxTr_8ODbZjxUtpyPKM4aGHWg2FC","2026-11-10_jogos_recomendados_20.csv","csv","1398","2026-11-11T19:25:16Z","Meu Drive/09 — OpenFree/09.1 — Sites, Favoritos e Projetos","me",False),
("1ws0i2T2UMjQQDDl6mkJhjIHo-72M-jel","2026-11-10_Favoritos_organizados_09-11-2026.html","html","888191","2026-11-11T19:24:45Z","Meu Drive/09 — OpenFree/09.1 — Sites, Favoritos e Projetos","me",False),
("1u2lnLDDZdbXyj9Foh6xVm_cSzzi-lCjz","2026-11-11_Conexões_Maçônicas_nas_Nações_Modernas.pptx","pptx","1615659","2026-11-11T19:23:52Z","Meu Drive/09 — OpenFree/09.1 — Sites, Favoritos e Projetos","me",False),
("1DZrBmdzBdQGMgXIjadT0Q6DjQLzDRwlw","2026-11-10_Apresentacao_Luck_Conjunto_Recomendado.pptx","pptx","85401","2026-11-11T19:23:22Z","Meu Drive/09 — OpenFree/09.1 — Sites, Favoritos e Projetos","me",False),
("1tGg_-RCgDmwPix_R_NfCeazNJi0Pb8kE8Ic4loWBkKA","2026-11-11_2._kit-planilha-memoria-de-elite.gsheet","gsheet","6955","2026-11-11T19:23:02Z","Meu Drive/09 — OpenFree/09.1 — Sites, Favoritos e Projetos","me",False),
("1oBwmYJkUj5hEIfQRT79UBkODmhe2O9zvSUOQzOVYCZY","2026-11-11_1._prompts-memoria-de-elite.gdoc","gdoc","10534","2026-11-11T19:22:47Z","Meu Drive/09 — OpenFree/09.1 — Sites, Favoritos e Projetos","me",False),
# 99.1
("1KrQSffeU8aE34jQi5XQqdzHD4mX8O7aB","2026-11-09_D074_TCLE-Tracionamento.docx","docx","23025","2026-11-11T19:26:59Z","Meu Drive/99 — Duplicados (nada foi apagado)/99.1 — Cópias excedentes","me",False),
("1lJIrjMwJkAcyxqp8hcqK9PxEAIsE6esb","2026-11-09_D070_TCLE-Exod-Protocolo.pdf","pdf","91221","2026-11-11T19:26:53Z","Meu Drive/99 — Duplicados (nada foi apagado)/99.1 — Cópias excedentes","me",False),
("1ebzYVXbzcexbzi4m9BZUmRNx9D_agawv","2026-06-25_D053_Obsidian_Knowledge_Pipeline.pptx","pptx","16829227","2026-11-11T19:25:51Z","Meu Drive/99 — Duplicados (nada foi apagado)/99.1 — Cópias excedentes","me",False),
("1WRy6YTqj6YtLIpRxqlj8IQfZdzeSFhdC","2026-11-09_D022_Contrato_Implante_MS_LGPD_CRO_20_paginas_carimbo_menor_linha_livre_MAIS_RECENTE.pdf","pdf","3896722","2026-11-11T19:23:57Z","Meu Drive/99 — Duplicados (nada foi apagado)/99.1 — Cópias excedentes","me",False),
("1o3tU7GcQXYnQ-No9-rQ-Zj7d6Y_O8ccO","2026-11-09_D021_CONTRATO_DE_PRESTAÇÃO_DE_SERVIÇOS_PROFISSIONAIS_MAIS_RECENTE.docx","docx","42105","2026-11-11T19:23:55Z","Meu Drive/99 — Duplicados (nada foi apagado)/99.1 — Cópias excedentes","me",False),
# Onlyoffice duplicado
("1yDC2UTQkgY5pMO2lyaUYJIKWaOZVqh1M","Onlyoffice-2026-08 — cópia (mod. 2026-10-13)","folder","","2026-11-09T20:40:47Z","Meu Drive/99 — Duplicados (nada foi apagado)/Onlyoffice-26-11-02 — DUPLICADO (cópia de 26-11_Arena; mod. mais recente 2026-10-13)","me",False),
("19ne3GACnQmXRG3cq1mOTwLQvS1SNDYlT","Onlyoffice-Uninass — cópia (mod. 2026-06-26)","folder","","2026-11-09T20:40:46Z","Meu Drive/99 — Duplicados (nada foi apagado)/Onlyoffice-26-11-02 — DUPLICADO (cópia de 26-11_Arena; mod. mais recente 2026-10-13)","me",False),
("1xuMQ6SI7wQRorvpObn0xevH4fxT6v8Su","Onlyoffice-Pesq-0001 — cópia (mod. 2026-06-25)","folder","","2026-11-09T20:40:45Z","Meu Drive/99 — Duplicados (nada foi apagado)/Onlyoffice-26-11-02 — DUPLICADO (cópia de 26-11_Arena; mod. mais recente 2026-10-13)","me",False),
("1-zjlqfyigHeXksuzcgtGJgV0x5p4CCL0","Onlyoffice-P-Aulas-Odonto — cópia (mod. 2026-07-08)","folder","","2026-11-09T20:39:08Z","Meu Drive/99 — Duplicados (nada foi apagado)/Onlyoffice-26-11-02 — DUPLICADO (cópia de 26-11_Arena; mod. mais recente 2026-10-13)","me",False),
("1CHQQQ0jMklDDcj7OdnNCt7HyHtcOgj8F",".DS_Store","bin","10244","2026-11-03T02:01:01Z","Meu Drive/99 — Duplicados (nada foi apagado)/Onlyoffice-26-11-02 — DUPLICADO (cópia de 26-11_Arena; mod. mais recente 2026-10-13)","me",False),
("1eLM1XF7EjyJU1-pYEXtQ-jotzq-qn1kX","NotebookLM-Templates-001.docx","docx","18566290","2026-06-26T17:14:26Z","Meu Drive/99 — Duplicados (nada foi apagado)/Onlyoffice-26-11-02 — DUPLICADO (cópia de 26-11_Arena; mod. mais recente 2026-10-13)","me",False),
# A Ordem e o Palco
("1fWTrDQNsRi1-WD8lBMCUWAhfNqgtl_ZU","A-Ordem-e-o-Palco.pptx","pptx","1780293","2026-11-11T17:54:27Z","Meu Drive/08 — Compartilhado/Maçonaria/A Ordem e o Palco","me",True),
("1Z-mF7sH5Qx2Mse3JkCzUZCAPkJD1YV05","A-Ordem-e-o-Palco.pdf","pdf","1794008","2026-11-11T17:54:18Z","Meu Drive/08 — Compartilhado/Maçonaria/A Ordem e o Palco","me",True),
]

# Merge avoiding duplicates by ID
existing_ids = set(i[0] for i in ITEMS)
for r in recent:
    if r[0] not in existing_ids:
        ITEMS.append(r)
        existing_ids.add(r[0])

print(f"Total ITEMS consolidated: {len(ITEMS)}")

# Save full inventory to drive-fase1/inventario_completo.csv
out_csv = ROOT / "inventario_completo.csv"
with open(out_csv, "w", newline="", encoding="utf-8") as f:
    w = csv.writer(f)
    w.writerow(["ID","nome","tipo","tamanho_bytes","localizacao_atual","data_modificacao","owner","compartilhado"])
    for id_, name, typ, size, mod, loc, owner, shared in sorted(ITEMS, key=lambda x: (x[5], x[1].lower())):
        w.writerow([id_, name, typ, size, loc, mod, owner, "sim" if shared else "nao"])

print("inventario_completo.csv gerado")

# Also need to handle Onlyoffice copies inner files - add them too
extra_inner = [
# 1yDC inner 6
("1xjkOajBQQ448dYBAkFDv2XmTBtzu-03S","Prp-Aulas-26-10-C.docx","docx","30788","2026-10-13T09:44:48Z","Meu Drive/99 — Duplicados (nada foi apagado)/Onlyoffice-26-11-02 — DUPLICADO (cópia de 26-11_Arena; mod. mais recente 2026-10-13)/Onlyoffice-2026-08 — cópia (mod. 2026-10-13)","me",False),
("1WgpJFONnkbQN_mB6H1DhthCIv2ZgbXYm","V2-Prpt-Convert-Ilustracao-ref.docx","docx","28372","2026-08-13T11:43:32Z","Meu Drive/99 — Duplicados (nada foi apagado)/Onlyoffice-26-11-02 — DUPLICADO (cópia de 26-11_Arena; mod. mais recente 2026-10-13)/Onlyoffice-2026-08 — cópia (mod. 2026-10-13)","me",False),
("1NPLG-XIgSZo087khai5EJt2QGpzKuamd","V2-Prpt-Converter-Vetor_em-Ultrarealista-ref.docx","docx","28860","2026-08-13T11:43:32Z","Meu Drive/99 — Duplicados (nada foi apagado)/Onlyoffice-26-11-02 — DUPLICADO (cópia de 26-11_Arena; mod. mais recente 2026-10-13)/Onlyoffice-2026-08 — cópia (mod. 2026-10-13)","me",False),
("1TU5NJpu_7eqMtL3ppzpwuAZpeqTJpJIt","Novo documento.docx","docx","8504","2026-08-13T11:39:42Z","Meu Drive/99 — Duplicados (nada foi apagado)/Onlyoffice-26-11-02 — DUPLICADO (cópia de 26-11_Arena; mod. mais recente 2026-10-13)/Onlyoffice-2026-08 — cópia (mod. 2026-10-13)","me",False),
("1fdQNvZ4zpsdnrZAzt-KTK1WaQcBHSQav","Sites-IA.docx","docx","46498","2026-07-08T09:07:12Z","Meu Drive/99 — Duplicados (nada foi apagado)/Onlyoffice-26-11-02 — DUPLICADO (cópia de 26-11_Arena; mod. mais recente 2026-10-13)/Onlyoffice-2026-08 — cópia (mod. 2026-10-13)","me",False),
("1KoaJieACjdsOlqGRAAQ9q8bJ-vwUmw1w","Aulas-Od.docx","docx","28845","2026-06-27T20:20:28Z","Meu Drive/99 — Duplicados (nada foi apagado)/Onlyoffice-26-11-02 — DUPLICADO (cópia de 26-11_Arena; mod. mais recente 2026-10-13)/Onlyoffice-2026-08 — cópia (mod. 2026-10-13)","me",False),
# 19ne inner
("1xNFBBfqABCZc3MAIsiKtPeMsddB3fk2l","PDFs2026","folder","","2026-11-03T02:50:51Z","Meu Drive/99 — Duplicados (nada foi apagado)/Onlyoffice-26-11-02 — DUPLICADO (cópia de 26-11_Arena; mod. mais recente 2026-10-13)/Onlyoffice-Uninass — cópia (mod. 2026-06-26)","me",False),
("1vI_vGKvY59W_XoXp24NQADJVbbeDh5mE","2026-2-Materias-Disponibilidade.docx","docx","30108","2026-06-26T17:05:14Z","Meu Drive/99 — Duplicados (nada foi apagado)/Onlyoffice-26-11-02 — DUPLICADO (cópia de 26-11_Arena; mod. mais recente 2026-10-13)/Onlyoffice-Uninass — cópia (mod. 2026-06-26)","me",False),
("1uZekLHZI19RGXckBt8PIZmAsLN_xLJpS","MAN-PED-01 - MIDDI - MANUAL INFORMATIVO DO DOCENTE E DO DISCENTE (2).pdf","pdf","4336921","2026-06-26T16:45:16Z","Meu Drive/99 — Duplicados (nada foi apagado)/Onlyoffice-26-11-02 — DUPLICADO (cópia de 26-11_Arena; mod. mais recente 2026-10-13)/Onlyoffice-Uninass — cópia (mod. 2026-06-26)/PDFs2026","me",False),
("1zoetRP3mcocigDLRoldS3QHfcPdDk_1R","HORÁRIO ATUALIZADO 2026.1 05.02 (1).pdf","pdf","257777","2026-06-26T16:45:14Z","Meu Drive/99 — Duplicados (nada foi apagado)/Onlyoffice-26-11-02 — DUPLICADO (cópia de 26-11_Arena; mod. mais recente 2026-10-13)/Onlyoffice-Uninass — cópia (mod. 2026-06-26)/PDFs2026","me",False),
("1VySadUAn20X1Zc6YmYyPo79JX3lfCFnV","GRA-MAT-0237-E - ODONTOLOGIA - ESTRUTURA CURRICULAR.pdf","pdf","166542","2026-06-26T16:45:14Z","Meu Drive/99 — Duplicados (nada foi apagado)/Onlyoffice-26-11-02 — DUPLICADO (cópia de 26-11_Arena; mod. mais recente 2026-10-13)/Onlyoffice-Uninass — cópia (mod. 2026-06-26)/PDFs2026","me",False),
("1OdIDfPkFDryngpeOPn-6dyaRdu2lfAMb","GRA-MAT-0237-F - ODONTOLOGIA - ESTRUTURA CURRICULAR.pdf","pdf","166945","2026-06-26T16:45:14Z","Meu Drive/99 — Duplicados (nada foi apagado)/Onlyoffice-26-11-02 — DUPLICADO (cópia de 26-11_Arena; mod. mais recente 2026-10-13)/Onlyoffice-Uninass — cópia (mod. 2026-06-26)/PDFs2026","me",False),
("1W5OMkpfQTM_fkiXtiqm_zNyNxRlLn5PJ","GRA-PLE-0237-E - ODONTOLOGIA - PLANO DE ENSINO.pdf","pdf","1603302","2026-06-26T16:45:14Z","Meu Drive/99 — Duplicados (nada foi apagado)/Onlyoffice-26-11-02 — DUPLICADO (cópia de 26-11_Arena; mod. mais recente 2026-10-13)/Onlyoffice-Uninass — cópia (mod. 2026-06-26)/PDFs2026","me",False),
("1ifUIi5HP5Ou-u5p7CJzRXpNKm6NIxO_N","GRA-PLE-0237-F - ODONTOLOGIA - PLANO DE ENSINO.pdf","pdf","1541529","2026-06-26T16:45:14Z","Meu Drive/99 — Duplicados (nada foi apagado)/Onlyoffice-26-11-02 — DUPLICADO (cópia de 26-11_Arena; mod. mais recente 2026-10-13)/Onlyoffice-Uninass — cópia (mod. 2026-06-26)/PDFs2026","me",False),
# 1xu inner
("1ZcKPW0SCSexcmkcQYhW-FzLAzcrstgnX","Cedula-Dolar","folder","","2026-11-03T02:50:51Z","Meu Drive/99 — Duplicados (nada foi apagado)/Onlyoffice-26-11-02 — DUPLICADO (cópia de 26-11_Arena; mod. mais recente 2026-10-13)/Onlyoffice-Pesq-0001 — cópia (mod. 2026-06-25)","me",False),
("1HIDB3lVT_-ta5jdpzOYLjzEWA-W4OkM-","PFN.docx","docx","2862716","2026-06-25T11:59:54Z","Meu Drive/99 — Duplicados (nada foi apagado)/Onlyoffice-26-11-02 — DUPLICADO (cópia de 26-11_Arena; mod. mais recente 2026-10-13)/Onlyoffice-Pesq-0001 — cópia (mod. 2026-06-25)","me",False),
("1gUtE2UZpG9drWjlk3CQF7dUoRWU8EVrc","Obsidian_Knowledge_Pipeline.pptx","pptx","16829227","2026-06-25T11:35:40Z","Meu Drive/99 — Duplicados (nada foi apagado)/Onlyoffice-26-11-02 — DUPLICADO (cópia de 26-11_Arena; mod. mais recente 2026-10-13)/Onlyoffice-Pesq-0001 — cópia (mod. 2026-06-25)","me",False),
("1cHSJ2yr4VlF-SVfjs0i9Nv0k--Ekhsnf","Pesquisa_Automot.docx","docx","4647953","2026-06-25T11:28:30Z","Meu Drive/99 — Duplicados (nada foi apagado)/Onlyoffice-26-11-02 — DUPLICADO (cópia de 26-11_Arena; mod. mais recente 2026-10-13)/Onlyoffice-Pesq-0001 — cópia (mod. 2026-06-25)","me",False),
("1rVeG0c2Gklk8i06QamNZm2bcbw3gZW4b","Anatomia_do_Dólar__Intaglio.mp4","mp4","61191156","2026-06-25T12:19:30Z","Meu Drive/99 — Duplicados (nada foi apagado)/Onlyoffice-26-11-02 — DUPLICADO (cópia de 26-11_Arena; mod. mais recente 2026-10-13)/Onlyoffice-Pesq-0001 — cópia (mod. 2026-06-25)/Cedula-Dolar","me",False),
("1eU2uTsdQ1WgTn2qk7bm_usBhfAi1sChc","Banknote_Design_Mastery.pptx","pptx","27528302","2026-06-25T12:19:28Z","Meu Drive/99 — Duplicados (nada foi apagado)/Onlyoffice-26-11-02 — DUPLICADO (cópia de 26-11_Arena; mod. mais recente 2026-10-13)/Onlyoffice-Pesq-0001 — cópia (mod. 2026-06-25)/Cedula-Dolar","me",False),
("1v4XbgcP1gEfyVc_1Dpk2qR7htyNu3JfK","A Arte da Gravura em Talho-Doce_ Guia de Prompts Técnico.docx","docx","8624","2026-06-25T12:19:26Z","Meu Drive/99 — Duplicados (nada foi apagado)/Onlyoffice-26-11-02 — DUPLICADO (cópia de 26-11_Arena; mod. mais recente 2026-10-13)/Onlyoffice-Pesq-0001 — cópia (mod. 2026-06-25)/Cedula-Dolar","me",False),
("1K1REvxabHkEwg4fv-FcoO_7XE9m2bEqY","A Arte e a Ciência da Gravura Monetária Americana.docx","docx","7184","2026-06-25T12:19:26Z","Meu Drive/99 — Duplicados (nada foi apagado)/Onlyoffice-26-11-02 — DUPLICADO (cópia de 26-11_Arena; mod. mais recente 2026-10-13)/Onlyoffice-Pesq-0001 — cópia (mod. 2026-06-25)/Cedula-Dolar","me",False),
("1GhK351rjbMmHu8Fz4_bnrIS8Y-OxC5ZG","Guia de Customização para Prompts Estilo Cédula.docx","docx","8056","2026-06-25T12:19:24Z","Meu Drive/99 — Duplicados (nada foi apagado)/Onlyoffice-26-11-02 — DUPLICADO (cópia de 26-11_Arena; mod. mais recente 2026-10-13)/Onlyoffice-Pesq-0001 — cópia (mod. 2026-06-25)/Cedula-Dolar","me",False),
("1i93wZKdLEyvpIZR4em8abl_ln5yc92Pi","Estilo-Cedula-Dolar.docx","docx","32308","2026-06-25T12:16:14Z","Meu Drive/99 — Duplicados (nada foi apagado)/Onlyoffice-26-11-02 — DUPLICADO (cópia de 26-11_Arena; mod. mais recente 2026-10-13)/Onlyoffice-Pesq-0001 — cópia (mod. 2026-06-25)/Cedula-Dolar","me",False),
]

for e in extra_inner:
    if e[0] not in existing_ids:
        ITEMS.append(e)
        existing_ids.add(e[0])

print(f"Total com inner: {len(ITEMS)}")
# rewrite inventory
with open(out_csv, "w", newline="", encoding="utf-8") as f:
    w = csv.writer(f)
    w.writerow(["ID","nome","tipo","tamanho_bytes","localizacao_atual","data_modificacao","owner","compartilhado"])
    for id_, name, typ, size, mod, loc, owner, shared in sorted(ITEMS, key=lambda x: (x[5], x[1].lower())):
        w.writerow([id_, name, typ, size, loc, mod, owner, "sim" if shared else "nao"])
print("inventario reescrito com inner")

# Save consolidated python for reuse
with open(ROOT/"inventario_consolidado.py","w",encoding="utf-8") as f:
    f.write("# Inventario consolidado Fase 1 - total itens\n")
    f.write(f"# Total {len(ITEMS)} itens verificados via API em 2026-11-21\n")
    f.write("ITEMS = [\n")
    for it in ITEMS:
        f.write(f"  {it!r},\n")
    f.write("]\n")
