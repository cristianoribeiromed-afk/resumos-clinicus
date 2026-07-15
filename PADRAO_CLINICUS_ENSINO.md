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

## 2.1 Primeiro feedback real de aluno — Cap. 46 (15/07/2026)

🟢 **Comprovado por aluna** (mensagem direta, 15/07/2026): ela prefere a **versão original** do Cap. 46 (antes da migração pro layout azul atual), especificamente porque *"visualmente tem mais pontos de atenção, que pode ajudar a fixar melhor"*.

Auditoria objetiva que confirma o motivo:

| Tipo de caixa | Cap.46 original | Cap.46 atual (azul) | Cap.47 | Cap.48 |
|---|---|---|---|---|
| 📌 `.prova` (cobrança de prova) | 4 | 0 | 0 | 0 |
| 💡 `.example` | 2 | 0 | 0 | 0 |
| ⚠️ `.hot` | 3 | 5 | 4 | 1 |
| 🎵 `.mnemo` | 3 | 2 | 2 | 1 |

A migração pro layout azul **perdeu** os tipos `.prova` e `.example` — presentes no original, ausentes em todos os capítulos atuais (46/47/48). Nenhum capítulo de Fisiologia II usa o sistema de cores validado do Vargas (`.analogy`/`.clinical`/`.criterio`) tampouco.

**Decisão:** reintroduzir `.prova` (cobrança de prova) e `.example` como caixas padrão em todo conteúdo de Fisiologia II, mantendo o layout visual azul atual (aprovado à parte) e o tom de escrita meio-termo (seção 1.4). Isso não substitui o sistema Vargas — ambos podem coexistir, cada um com seu propósito.

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
| 15/07/2026 | Primeiro feedback real de aluna sobre Cap.46 — prefere versão original por ter mais "pontos de atenção" | 🟢 aluna |
| 15/07/2026 | Reintroduzir `.prova` e `.example`, adicionar sistema Vargas ao Cap.46/47/48 | ✅ decisão conjunta |

