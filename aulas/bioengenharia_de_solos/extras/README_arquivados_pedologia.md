# Arquivos Preservados em `extras/` — Bioengenharia de Solos

Esta pasta armazena versões originais e recortes pedagógicos de aulas que extrapolavam o escopo técnico de **Bioengenharia de Água e Solo / Conservação do Solo e da Água** (pertencendo a disciplinas de *Pedologia Geral / Gênese e Classificação do Solo* ou *Manejo de Solos Afetados por Sais*), bem como backups anteriores à higienização de OCR.

## Arquivos preservados nesta pasta:
1. `original_01_solos_aridos_halomorficos_buringh.qmd`:
   - Conteúdo original da Aula 01 baseado em P. Buringh (1970) sobre *Aridisols* (Soil Taxonomy USDA), pavimento desértico (*regs*), *Solonchak*, *Solonetz*, ciclo de solodização e manejo de irrigação em solos salinos/sódicos.
   - **Destinação recomendada:** Disciplina de *Pedologia / Gênese e Classificação do Solo* ou *Manejo de Irrigação e Salinidade*.
2. `original_02_intemperismo_geral.qmd`:
   - Versão anterior da Aula 02 contendo slides de crioclastia (congelamento de água em fendas alpinas a $0\ ^\circ\text{C}$) e geoquímica de rochas proterozoicas.
   - **Destinação recomendada:** Disciplina de *Geologia Agrícola / Geomorfologia Geral*.
3. `original_03_o_solo_ufs.qmd`:
   - Backup da conversão bruta de slides da UFS (`Cincias do Solos III`) antes da correção de OCR e integração dos indicadores físico-mecânicos e de qualidade do solo (oriundos de `aulas/analise_ambiental/extras/original_12.1_qualidade_solo_agronomia.qmd`).
4. `gerar_figuras_bioengenharia.py`:
   - Script Python reprodutível que gera os 5 diagramas técnicos em alta resolução (`.png` 300 dpi + `.svg`) na pasta `img/` da raiz do repositório (`bs_*.png` / `bs_*.svg`). Os caminhos são relativos ao script; as curvas numéricas estão identificadas como ilustrações, sem calibração de solos ou espécies.

## Integração dos recortes de Análise Ambiental

Os arquivos de origem permanecem em [Análise Ambiental — extras](../../analise_ambiental/extras/). A implementação nesta disciplina usa os temas abaixo com métodos, unidades, exemplos e limites de interpretação explícitos.

| Origem preservada | Destino em Bioengenharia | Integração |
|---|---|---|
| [Qualidade do solo — ex-12.1](../../analise_ambiental/extras/original_12.1_qualidade_solo_agronomia.qmd) | [Aula 03 — O Solo](../aulas/03_fisica_mecanica_qualidade_solo/fisica_mecanica_qualidade_solo.qmd) | Densidade, porosidade, mesa de tensão, agregação, RP, infiltração, CBM, respiração, qCO₂, enzimas e IQS |
| Mesmo recorte de qualidade | [Aula 14 — Biomantas](../aulas/14_biomantas_geossinteticos/biomantas_geossinteticos.qmd) | Indicadores de solo, vegetação e sedimento no monitoramento |
| [Bioengenharia geotécnica — ex-14.1](../../analise_ambiental/extras/original_14.1_bioengenharia_geotecnica.qmd) | [Aula 01 — Fundamentos nos trópicos](../aulas/01_solos_tropicais_fundamentos_bioengenharia/solos_tropicais_fundamentos_bioengenharia.qmd) | Funções hidrológicas, mecânicas e ecológicas; seleção regional de espécies e acompanhamento |
| Mesmo recorte geotécnico | [Aula 09 — Modelagem e biomecânica](../aulas/09_raizes_ensaios_modelagem_3d/raizes_ensaios_modelagem_3d.qmd) | Tração e arrancamento, alometria, RAR, contribuição radicular e suas limitações |
| [Síntese dos recortes](../../analise_ambiental/extras/conteudos_extras_outras_disciplinas.qmd) | Aulas 01, 03, 09 e 14 | Articulação entre diagnóstico, dimensionamento e monitoramento |

O material de paisagem cultural continua no acervo de origem; não foi incorporado a Bioengenharia de Solos.

## Ajustes da sequência de aulas

- Aulas 01–04: perfil tropical, intemperismo, diagnóstico físico e biológico, mecânica do solo, processos erosivos e hidrologia.
- Aulas 05–08: texto de OCR substituído, calibração e nivelamento, EV/EH, armazenamento, vazão, Manning, resistência à erosão e exercício completo em Planossolo.
- Aula 09: distinção entre envelope 3D e volume de raízes; seção de RAR; ensaios independentes; conversões MPa/kPa e porcentagem/fração.
- Aula 11: caminho da imagem de escavação conferido; a ligação com espaço codificado já estava correta na versão recebida.
- Aula 18: repetição introdutória de riprap substituída por acoplamento da proteção de base à fundação da Krainer, filtros e monitoramento de solapamento.
- Aulas 19 e 21: referências e diagramas sincronizados com as 21 aulas, incluindo Canaleta Verde como Aula 20.
- [Portal](../../../teaching/bioengenharia-de-solos/index.qmd) e [plano](../../../teaching/bioengenharia-de-solos/plano.qmd): tópicos, referências das atividades e sequência sincronizados. Os formulários externos foram mantidos.

Os cabeçalhos das apresentações, a configuração do projeto e os estilos foram preservados. Os arquivos originais arquivados não integram a renderização das aulas; suas figuras permanecem nas pastas de imagens das respectivas aulas.

## Critérios usados na revisão técnica

- Limiares de RP, densidade, porosidade e resistência hidráulica exigem contexto; não foram tratados como limites universais.
- A umidade ótima de Proctor não foi equiparada ao intervalo plástico de Atterberg.
- RUSLE, vazão de pico e volume escoado foram distinguidos, assim como seus alcances.
- Nos canais, capacidade e velocidade de Manning são verificadas na mesma seção, com sensibilidade à rugosidade e compatibilidade do perfil longitudinal.
- Valores de curvas, cenários e coesão radicular destinados a exercícios foram identificados como didáticos.

Fontes principais: [Embrapa — métodos de análise](https://www.embrapa.br/web/solos/busca-de-publicacoes/-/publicacao/1085209/manual-de-metodos-de-analise-de-solo), [USDA-NRCS — projeto de canais](https://directives.nrcs.usda.gov/sites/default/files2/1712931093/7332.pdf), [USDA-NRCS — bioengenharia fluvial](https://directives.nrcs.usda.gov/sites/default/files2/1720623369/Technical%20Supplement%2014%20I%20-%20Streambank%20Soil%20Bioengineering.pdf), [USDA-ARS — RUSLE2](https://www.ars.usda.gov/ARSUserFiles/60600505/rusle/rusle2_science_doc.pdf) e [Waldron (1977)](https://doi.org/10.2136/sssaj1977.03615995004100050005x).
