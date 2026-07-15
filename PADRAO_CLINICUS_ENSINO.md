# Padrão Clinicus de Ensino

**Versão 1** — criado em 14/07/2026, a partir do que já tem prova real de funcionar (elogios de alunos + validação do Dr. Cristiano), não de suposição.

Este documento é a referência fixa pra todo conteúdo novo da plataforma. Qualquer mudança de formato precisa passar pelo processo descrito no final antes de ir pra um arquivo publicado.

---

## 1. Estrutura de abas (obrigatória)

| Aba | Conteúdo | Status |
|---|---|---|
| 📋 Guia de Estudo | Conteúdo teórico, tom conversacional | ✅ Padrão |
| 🩺 Casos Clínicos | Caso progressivo (2-3 fases reveladas aos poucos) | ✅ Padrão |
| 🃏 Flashcards | Motor SM-2 (revisão espaçada, localStorage) | ✅ Padrão |
| ✅ Banco de Questões | MCQ comentadas, gabarito balanceado | ✅ Padrão |
| 🎮 Quiz Rápido | Versão curta pra revisão relâmpago | ✅ Padrão |
| 🗺️ Mapas Mentais | — | ❌ **Removida do padrão** (ver seção 5) |

---

## 2. Tom de escrita

Baseado no que rendeu elogio real no Capítulo 47:

- **Segunda pessoa, sempre** ("você", nunca "o aluno deve...")
- Analogias do cotidiano antes da definição técnica
- Frases curtas. Parágrafo longo é sinal de que precisa quebrar em tópicos
- Pergunta retórica pra abrir seção é bem-vinda ("Por que você para de sentir a roupa no corpo?")
- Gíria/expressão brasileira coloquial é permitida com moderação ("bate o cotovelo naquele osso da risada")

## 3. Sistema visual

- **Fonte base: 18px** (não 16px — telas menores cansam a vista, confirmado por feedback direto)
- Tema escuro, paleta por disciplina (cada matéria pode ter sua cor de destaque, mas segue a mesma estrutura)
- **Caixinha de 4 cores (al-grid)** — usar em pontos de alta densidade de informação:
  - ✅ verde — O que você deve lembrar
  - ⚠️ coral — Erro comum
  - ⚡ azul — Questão rápida (com resposta escondida em toggle)
  - 🧠 roxo — Autoexplicação
  - Meta: pelo menos 1 a cada 2-3 seções principais do Guia de Estudo
- **Shell de navegação** (cabeçalho fixo + sidebar da disciplina + breadcrumb + progresso + anterior/próximo) — implementado em toda a plataforma, manter em todo conteúdo novo via `inject_shell.py`

## 4. Flashcards — meta de completude

- **Mínimo de 30 cards por capítulo** (referência: Cap. 46 tem 34, foi elogiado; Cap. 47 tinha só 20, foi criticado como "incompleto")
- Motor SM-2 com 3 botões de review (Não lembrei / Com esforço / Fácil) — não mexer nesse mecanismo, já está validado
- Cobrir: definições-chave, números/valores que caem em prova, armadilhas conceituais, e pelo menos 1 card por caso clínico

## 5. Mapas Mentais — status: EM ABERTO, não obrigatório

Duas tentativas até agora, nenhuma aprovada:
1. **Formato ASCII/fluxograma de texto** (Cap. 46 e outros) — reclamação original: "não é mapa mental de verdade"
2. **Formato SVG radial** (tentativa nesta sessão, Cap. 47) — não agradou visualmente

**Decisão:** não incluir "Mapas Mentais" como aba obrigatória em conteúdo novo até termos um formato validado. Se o tema pedir uma representação visual, usar diagrama de fluxo simples dentro do Guia de Estudo mesmo (não como aba separada), ou pular essa parte.

## 6. Processo pra testar formato novo (regra nova, por causa do que aconteceu)

**Nunca mais redesenhar um elemento visual direto num arquivo já publicado sem aprovação prévia.** A partir de agora:

1. Construir 1 protótipo isolado (não no arquivo de produção)
2. Mostrar pro Dr. Cristiano com um resumo claro do que mudou e por quê
3. Só aplicar em conteúdo publicado depois do "sim"
4. Se aprovado, documentar aqui como novo padrão

---

## Histórico de decisões

| Data | O que mudou | Motivo |
|---|---|---|
| 14/07/2026 | Fonte base 16px → 18px | Feedback direto: letra pequena |
| 14/07/2026 | Adicionado al-grid (4 cores) no padrão | Elogiado no material da Profa. Deborah |
| 14/07/2026 | Mapas Mentais removidos da lista obrigatória | Duas tentativas reprovadas (ASCII e SVG) |
| 14/07/2026 | Meta de 30+ flashcards por capítulo | Cap. 47 com 20 foi sentido como incompleto |
