# Padrão Clinicus de Ensino

**Versão 2** — corrigida em 14/07/2026. A v1 continha um erro: atribuía validação de alunos ao Capítulo 46 de Fisiologia II, mas **nenhum aluno teve acesso a esse material ainda**. Essa versão separa claramente 3 tipos de fonte, pra nunca mais confundir:

- 🟢 **Comprovado por alunos** — elogio real, de gente que usou
- 🔵 **Feedback direto do Dr. Cristiano** — validado por ele, mas não testado com aluno
- 🟡 **Recomendação minha (orientador pedagógico)** — síntese, ainda não validada por ninguém — tratar como sugestão, não regra

---

## 1. A referência real: Bioquímica — Prof. Robert Vargas Bernal

🟢 Esse é o material com elogio confirmado de alunos, especificamente por: **cores, organização, e o modelo de flashcard estilo Anki**. Arquivos: `bioquimica_vargas_*.html`.

### 1.1 Sistema de cores (multi-semântico, não um grid fixo)

Não é uma caixinha de 4 cores agrupada — são **4 tipos de caixa usados individualmente, onde fizer sentido no texto**, cada uma com um propósito claro:

| Classe CSS | Cor | Uso |
|---|---|---|
| `.analogy` | dourado | Analogia do dia a dia pra explicar o conceito |
| `.clinical` | vermelho | Correlação clínica |
| `.mnemo` | azul | Mnemônico / truque de memorização |
| `.criterio` | verde | Critério técnico exato / exceção que cai em prova |

Paleta base: `--green1:#6bbf59; --green2:#a3d84a; --gold:#ffd166; --red:#ff5c6c; --blue:#4d9fff` sobre fundo escuro `#0d0f16`. Tipografia: **Lora** (serifada) pros títulos, **DM Sans** pro corpo do texto — essa combinação séria+legível parece parte do que funciona.

### 1.2 Organização — trilha de progresso visível

Uma barra pequena, dentro da área de abas, mostra a sequência inteira do capítulo com setas: `Estrutura → Classificação → Nomenclatura → Propriedades → Funções → Flashcards → Quiz`. Isso dá ao aluno noção de "onde estou, o que falta" sem precisar abrir a sidebar. **Vale adotar em todo conteúdo novo.**

### 1.3 Flashcards estilo Anki

🟢 Comprovado: botões com os rótulos genuínos do Anki (**De novo / Difícil / Bem / Fácil**), contador "Cartão X/Y", contador de "Dominados", e botão de **misturar (🔀)**.

⚠️ Detalhe técnico importante: essa versão **não tem repetição espaçada de verdade** — não salva intervalo nem data de próxima revisão, só soma XP e conta "dominados" na sessão. Quem tem o algoritmo real (SM-2 com localStorage, intervalos calculados) é o material de Fisiologia II — só que com rótulos genéricos ("Não lembrei / Com esforço / Fácil"), não os do Anki.

🟡 **Minha recomendação:** juntar os dois — manter o algoritmo real de repetição espaçada (SM-2, o que já existe em Fisiologia) mas trocar os rótulos dos botões pros 4 termos genuínos do Anki (De novo/Difícil/Bem/Fácil) e adicionar o botão de misturar + contador de dominados.

✅ **APROVADO em 14/07/2026** — protótipo testado (com prévia de "daqui a quantos dias volta" em cada botão) e validado pelo Dr. Cristiano. Passa a ser o padrão pra flashcards em conteúdo novo e na próxima atualização dos capítulos existentes.

---

## 1.4 Tom de escrita — o meio-termo (definido em 14/07/2026)

Comparação direta feita entre os dois estilos:

- **Vargas (🟢 comprovado):** terceira pessoa, registro professor-sério, preciso, com analogia pontual. Ex: *"Aminoácidos são compostos orgânicos que se combinam para formar proteínas... os 'sillares' (tijolos) que as constroem."*
- **Fisiologia Cap. 47 (🔵 só feedback do Dr. Cristiano, não testado):** segunda pessoa o tempo todo, bem coloquial. Ex: *"você bate o cotovelo naquele 'osso da risada'..."*

**Decisão:** usar o registro do Vargas como base (é o que tem prova), com pitada de didática:

- **Base:** direto, preciso, terceira pessoa na maior parte do texto
- **Segunda pessoa ("você"):** só nos momentos de virada — quando o capítulo revela algo contraintuitivo ou é o ponto mais importante da seção. Não o texto inteiro.
- **Pergunta retórica:** ok pra abrir uma seção difícil, com moderação — não em toda seção
- **Evitar:** gírias muito regionais/informais (tipo "osso da risada"). Prefere clareza a graça.

Essa orientação vale a partir de agora pra todo conteúdo novo — inclusive o próximo capítulo que o Dr. Cristiano for mandar.

---

## 2. Feedback direto do Dr. Cristiano (não testado com aluno ainda)

🔵 Sobre o material de Fisiologia II (Cap. 46/47), especificamente:

- **Fonte pequena demais** — corrigido pra 18px de base no Cap. 47. Isso NÃO é algo que o material do Vargas também faz (ele usa tamanho padrão ~16px) — é uma correção pontual baseada no seu incômodo direto, não uma cópia de outro material.
- **Mapas Mentais não funcionam** — nem o formato ASCII (usado em várias disciplinas, incluindo Cap. 46) nem a tentativa em SVG (Cap. 47) agradaram. Ver seção 4.

## 2.1 Primeiro feedback real de aluna — Cap. 46 (15/07/2026)

🟢 **Comprovado por aluna** — a primeira validação real de estudante que esse capítulo recebe (corrige a nota da v1/v2 que dizia que nenhum aluno tinha acesso ainda). Mensagem literal: *"eu prefiro esse primeiro, acho que visualmente tem mais pontos de atenção, que pode ajudar a fixar melhor"* — comparando a versão **original** do Cap. 46 (pré-redesign, layout vermelho) com a versão **atual** (layout azul, em produção).

**Auditoria objetiva que confirma o feedback** (contagem de caixas de destaque):

| Tipo de caixa | Cap.46 original | Cap.46 atual (produção) | Cap.47 | Cap.48 |
|---|---|---|---|---|
| 📌 `.prova` (cobrança de prova) | 4 | 0 | 0 | 0 |
| ⚠️ `.hot` (alerta/confusão comum) | 3 | 5 | 4 | 1 |
| 💡 `.example` | 2 | 0 | 0 | 0 |
| 🎵 `.mnemo` | 3 | 2 | 2 | 1 |
| 🧠 `.al-box` (autoexplicação) | 0 | 0 | 12 | 8 |
| `.analogy`/`.clinical`/`.criterio` (sistema Vargas 🟢) | 0 | 0 | 0 | 0 |

**Conclusão:** o redesign pro layout azul perdeu os tipos `.prova` e `.example`, que não foram recriados em nenhum capítulo posterior. Nenhum capítulo de Fisiologia II usa o sistema de cores validado do Vargas (seção 1.1), apesar de estar documentado como padrão.

**Decisão (15/07/2026):** reintroduzir `.prova` e `.example` como caixas padrão em todo conteúdo de Fisiologia II (novo e existente), mantendo `.hot` e `.mnemo`, e adicionar o sistema Vargas (`.analogy`/`.clinical`/`.criterio`) que estava documentado mas nunca aplicado aqui. O layout visual azul do Cap. 46 atual permanece — a mudança é de densidade/tipos de caixa de destaque, não de identidade visual.

**Status de aplicação real (15/07/2026):** Cap. 46 e Cap. 4 (48 parte 2) já têm `.prova`/`.example`/sistema Vargas. Cap. 47 e Cap. 48 (parte 1) ainda **não** têm — pendente.

## 2.2 Estratégia de simulados — sem simulado por capítulo (15/07/2026)

✅ **Decisão do Dr. Cristiano:** Fisiologia II **não terá simulado em cada capítulo individual**. Os capítulos ficam só com Banco de Questões (comentado) + Quiz Rápido, como já é o padrão. O **simulado será único e integrado**, cobrindo o conteúdo completo de P1, construído **só depois que todos os capítulos de P1 estiverem prontos** — não capítulo a capítulo.

Motivo: preservar a possibilidade de vender o simulado como produto separado do guia de estudo (mesmo modelo de monetização já usado em Bioquímica e Biologia I — capítulo/resumo é um produto, simulado é outro).



---

## 3. Estrutura de abas (padrão em uso, sem reclamação registrada)

| Aba | Conteúdo |
|---|---|
| Guia de Estudo | Conteúdo teórico |
| Casos Clínicos | Caso progressivo (quando aplicável) |
| Flashcards | Ver seção 1.3 |
| Banco de Questões / Quiz | MCQ comentadas, gabarito sempre balanceado (regra permanente, não muda) |

## 4. Mapas Mentais — status: EM ABERTO

Duas tentativas reprovadas (ASCII e SVG radial). Não incluir como aba obrigatória em conteúdo novo até termos uma versão validada.

## 5. Processo pra testar formato novo

**Nunca redesenhar um elemento visual direto num arquivo já publicado.**

1. Construir 1 protótipo isolado
2. Mostrar pro Dr. Cristiano com o que mudou e por quê — e deixar claro se é 🟢 comprovado, 🔵 feedback seu, ou 🟡 sugestão minha
3. Só aplicar em conteúdo publicado depois do "sim"
4. Documentar aqui como novo padrão, com a fonte certa (não inventar validação que não existe)

---

## Histórico de decisões

| Data | O que mudou | Fonte |
|---|---|---|
| 14/07/2026 | v1 criada, com erro (atribuiu elogio ao Cap. 46 sem alunos terem acesso) | — |
| 14/07/2026 | v2: corrigida a fonte real do elogio pra Bioquímica do Prof. Vargas | 🟢 Dr. Cristiano confirmou |
| 14/07/2026 | Fonte base 18px no Cap. 47 | 🔵 feedback direto |
| 14/07/2026 | Mapas Mentais fora da lista obrigatória | 🔵 duas tentativas reprovadas |
| 14/07/2026 | Sistema de cores multi-semântico (não grid fixo) documentado | 🟢 Bioquímica Vargas |
| 14/07/2026 | Trilha de progresso nas abas documentada como boa prática | 🟢 Bioquímica Vargas |
| 14/07/2026 | Sugestão: SM-2 real + rótulos/UX do Anki | 🟡 sugestão minha |
| 14/07/2026 | Flashcard SM-2+Anki aprovado após protótipo testado | ✅ aprovado pelo Dr. Cristiano |
| 14/07/2026 | Tom de escrita: meio-termo (base Vargas + você nos momentos de virada) | ✅ decisão conjunta |
| 15/07/2026 | Primeiro feedback real de aluno no Cap. 46: prefere versão original por ter mais caixas de destaque (`.prova`/`.example`) | 🟢 aluna, mensagem direta |
| 15/07/2026 | Reintrodução de `.prova` e `.example` como padrão em Fisiologia II | ✅ decisão do Dr. Cristiano |
| 15/07/2026 | Sem simulado por capítulo em Fisiologia II — simulado único e integrado, construído só após P1 completo | ✅ decisão do Dr. Cristiano |
| 15/07/2026 | Materia renomeada para "Fisiología II — Prof. Gabriel Coronil" (coexistência futura com versão do Prof. Lisandro) | ✅ decisão do Dr. Cristiano |
| 15/07/2026 | **P2 de Fisiología II completa: 11 capítulos** (Cap. 46-49, 55, 63-66 do Guyton) — bloco sensorial/reflexos + bloco gastrointestinal inteiros publicados e sincronizados | 🏁 marco concluído |
| 15/07/2026 | Primeiro feedback real de aluna sobre Cap.46 — prefere versão original por ter mais "pontos de atenção" | 🟢 aluna |
| 15/07/2026 | Reintroduzir `.prova` e `.example`, adicionar sistema Vargas ao Cap.46/47/48 | ✅ decisão conjunta |


---

## 6. Correção: SM-2 real + interface Anki já estava aplicado (16/07/2026)

⚠️ A seção 1.3 dizia que a combinação "SM-2 real + rótulos genuínos do Anki + prévia de dias em cada botão" ainda não tinha sido aplicada em nenhum capítulo publicado, só aprovada em protótipo. **Isso estava desatualizado.** Conferido em 16/07/2026: `Capitulo_04_Especializacoes_Membrana_Basal.html` (Histologia I) já tem essa combinação completa e publicada — 4 rótulos (De novo/Difícil/Bem/Fácil), 4 níveis de qualidade no algoritmo, prévia de dias em cada botão.

**Correção:** esse já é o padrão em uso, não mais "pendente de primeira aplicação". `Capitulo_08_Especializacoes_Epitelio.html` (Histologia I, P2 — criado em 16/07/2026) reutiliza o mesmo motor, não é a primeira aplicação.

## 7. Achado à parte: título errado no Capítulo 4 (16/07/2026)

🐛 `Capitulo_04_Especializacoes_Membrana_Basal.html`, arquivado em `semestre-01/histologia1/`, tem `<title>Bioquímica II — Cap. 4: ...</title>` — a tag `<title>` do navegador está com a disciplina errada. O conteúdo em si é de Histologia I (confirmado pelos tópicos: domínio apical, complexo de união, membrana basal). Não corrigido ainda — só registrado, porque não fazia parte do pedido desta rodada e mexer em arquivo já publicado sem pedido explícito vai contra a regra da seção 5.

## 8. Imagem real extraída do material fonte (16/07/2026)

✅ **Decisão do Dr. Cristiano:** sempre que o material fonte (slide, apostila, PDF) tiver diagrama, tabela colorida ou infográfico bem feito, a imagem real deve ser recortada do material e inserida no capítulo — não recriada como texto ou tabela. Aplica-se a partir de agora em todo conteúdo novo.

**Processo seguido no Capítulo 8 (Especializações do Epitélio):** das imagens disponíveis no material fonte (apresentação em pptx, 45 imagens embutidas), 3 foram selecionadas por critério de qualidade didática (diagrama esquemático claro ou micrografia sem marca d'água/branding de terceiro) e o restante descartado — inclusive uma imagem de endoscopia com marca d'água de site e de aparelho médico, que não serve pro padrão. As 3 aprovadas foram salvas em `assets/histologia1/` e linkadas no capítulo com `<figcaption>` explicando o que a imagem mostra.

## Histórico de decisões (continuação)

| Data | O que mudou | Fonte |
|---|---|---|
| 16/07/2026 | Correção: SM-2+Anki+prévia já estava em uso desde o Cap. 4 de Histologia I, não era mais "pendente de primeira aplicação" | 🟢 conferido no arquivo publicado |
| 16/07/2026 | Achado: título do Cap. 4 de Histologia I diz "Bioquímica II" por engano — não corrigido, só registrado | 🐛 achado, não solicitado |
| 16/07/2026 | Imagem real recortada do material fonte, em vez de recriar como texto — padrão a partir de agora | ✅ decisão do Dr. Cristiano |
| 16/07/2026 | Capítulo 8 de Histologia I criado (P2 — Especializações do Epitélio), primeiro capítulo novo da P2 | 🏁 marco concluído |

| 16/07/2026 | Capítulos 9, 10 e 11 de Histologia I criados (P2: Tecido Conectivo, Tecido Adiposo, Tecido Sanguíneo) | 🏁 marco concluído |
| 16/07/2026 | **P2 de Histologia I completa: 4 capítulos novos (Cap. 8-11)**, cobrindo Especializações do Epitélio, Tecido Conectivo, Tecido Adiposo e Tecido Sanguíneo -- todos com imagem real curada do material fonte (nenhuma recriada como texto) | 🏁 marco concluído |
## 9. Regra editorial: checar lógica dos dados extraídos, perguntar em caso de dúvida (22/09/2026)

🐛 **Erro real que motivou essa regra:** no Capítulo 2 de Epidemiología — CDE, os Programas PAIS (Atenção Integral por Etapa da Vida) foram publicados com "Adolescente: 10-19 anos" e "Adulto: 20-24 anos" — copiado direto do PDF fonte, sem checar a lógica. Isso deixava um buraco de 25 a 64 anos sem NENHUM programa cobrindo (já que "Adulto Mayor" só começa aos 65). O Dr. Cristiano identificou o erro e corrigiu: Adolescente é 10-24, Adulto é 25-64.

✅ **Regra editorial, a partir de agora:** ao extrair QUALQUER dado numérico, faixa etária, percentual, sequência ou classificação de um material fonte (PDF, slide, apostila), checar se a informação faz sentido LÓGICO antes de publicar — não só copiar o que está escrito. Se a checagem levantar dúvida real (número que não fecha, faixa com buraco, sequência que não bate, dado que contradiz outro já publicado) e não for possível resolver sozinho com confiança, **perguntar ao Dr. Cristiano antes de publicar** — não publicar algo duvidoso "torcendo pra estar certo", mesmo que isso signifique atrasar a entrega daquele trecho específico.

| Data | O que mudou | Fonte |
|---|---|---|
| 22/09/2026 | Regra editorial: checar lógica dos dados extraídos de material fonte antes de publicar; em caso de dúvida real, perguntar ao Dr. Cristiano antes de publicar | ✅ decisão do Dr. Cristiano, motivada por erro real (faixas etárias dos Programas PAIS) |


| 17/07/2026 | Capitulos 56 e 57 de Fisiologia II criados (Sistema Nervoso Motor; Cerebelo e Ganglios Basais) -- pulado o material que ja estava coberto pelo Cap. 55 (reflexos medulares), evitando duplicar | 🏁 marco concluido |
| 17/07/2026 | **Pendencia registrada, nao esquecer**: a barra lateral de navegacao (`cmed-nav-sidebar-list`) so foi atualizada nos proprios Cap. 56 e 57 -- os outros 12+ capitulos ja publicados de Fisiologia II (38 ao 66) ainda NAO linkam pro Cap. 56/57. Precisa de uma passada em cada arquivo existente pra manter a navegacao entre capitulos consistente | 🔴 pendencia real, nao feita |
| 17/07/2026 | Banco de Questoes do Cap. 56/57 replicou o formato profundo do Cap. 46 (justificativa + analise individual de cada alternativa errada + conceito + pegadinha + dica) -- 6 questoes cada, nao 10, por escopo da sessao | 🟡 nivel aplicado, volume menor que a media historica |
| 17/07/2026 | Caso Clinico do Cap. 56/57 tem só 1 nivel, nao os 3 niveis progressivos do Cap. 46 -- e Mapa Mental ficou de fora dos dois, dado o status contestado (rejeitado no padrao escrito, mas presente no Cap. 46 de verdade) | 🟡 decisao de escopo, nao definitiva |


## 9. Achado sério: padrão de gabarito previsível (17/07/2026)

🔴 **Bug real, encontrado pelo Dr. Cristiano, não por revisão própria.** Todos os capítulos criados nesta sessão (Cap. 8-11 de Histologia I, Cap. 56-57 de Fisiologia II) tinham a resposta certa concentrada quase toda numa letra só, ou faltando letras inteiras:

| Capítulo | Antes da correção |
|---|---|
| Cap. 8 (Histologia) | B: 6, C: 4 — nunca A, nunca D |
| Cap. 9 (Histologia) | B: 7, A: 2, C: 1 — nunca D |
| Cap. 10 (Histologia) | B: 5, A: 2, C: 1 — nunca D |
| Cap. 11 (Histologia) | B: 5, C: 3, A: 2 — nunca D |
| Cap. 56 (Fisiologia) | **A: 6 de 6** — toda questão do banco tinha resposta A |
| Cap. 57 (Fisiologia) | **A: 6 de 6** — mesmo problema |

Isso é um problema sério de qualidade de avaliação -- um aluno que percebe o padrão consegue pontuar bem sem saber o conteúdo. Não era intencional, veio de escrever a alternativa certa sempre na mesma posição ao redigir, sem embaralhar depois.

**Corrigido**: reorganizadas as alternativas de cada questão (trocando a POSIÇÃO do texto certo, não só o índice), com o cuidado de também realinhar a analise/analise_letters no formato de Banco de Questões (pra explicação de cada alternativa errada continuar apontando pra alternativa certa depois da troca -- verificado manualmente numa amostra antes de publicar).

**Regra nova, valendo a partir de agora**: ao escrever qualquer Quiz Rápido ou Banco de Questões, a posição da resposta certa precisa variar entre as questões -- nunca redigir todas com a certa na mesma letra, e idealmente conferir a distribuição (contagem por letra) antes de publicar, não confiar que "vai dar variado sozinho".
