# -*- coding: utf-8 -*-
import re, sys

def strip_shell(path):
    with open(path, encoding='utf-8') as f:
        html = f.read()

    if 'cmed-nav-header' not in html:
        print(f"  {path}: sem shell, pulando")
        return False

    # remove o link do CSS
    html = html.replace('<link rel="stylesheet" href="/assets/shell-nav.css">\n', '', 1)

    # remove o bloco do topo: novo toolbar (modo leitura+temas+progresso) OU botao antigo (se existir) + header ate cmed-nav-main
    html = re.sub(
        r'(?:<div class="cmed-reading-toolbar">.*?</div>\n<button class="cmed-reading-top".*?</button>\n<div class="cmed-reading-progress".*?></div>\n)?(?:<button class="cmed-reading-btn".*?</button>\n)?<header class="cmed-nav-header">.*?<div class="cmed-nav-main">\n',
        '',
        html, count=1, flags=re.DOTALL
    )

    # remove o bloco do rodape: do fechamento do cmed-nav-main ate o fim de TODOS
    # os scripts do rodape (toggle mobile + modo leitura + os 5 <script src=/assets/...>).
    # IMPORTANTE: vai ate logo antes de </body> (lookahead), nao ate o 1o/2o </script> --
    # isso evita que <script src=...> sobrem sem ser removidos e sejam duplicados
    # a cada novo ciclo de strip+inject (bug que causava scripts repetidos 6-9x).
    html = re.sub(
        r'\n  </div>\n</div>\n<nav class="cmed-nav-prevnext">.*?(?=</body>)',
        '\n',
        html, count=1, flags=re.DOTALL
    )

    # limpeza de orfaos: ciclos antigos (antes do fix acima) deixavam grupos soltos
    # dos 5 <script src=/assets/...> SEM o wrapper </div></div><nav prevnext>, porque
    # o regex de rodape antigo so removia ate o 1o/2o </script>. Esses grupos ficam
    # ANTES do anchor mais recente e nao sao pegos pelo regex acima -- remove todos
    # aqui, de forma idempotente (nunca deveriam existir soltos no "conteudo").
    orfao_pattern = (
        r'(?:\n?<script src="/assets/(?:clinicus-storage|focus-pomodoro|progress-tracker|pdf-export|pwa-register)\.js" defer></script>)+\n?'
    )
    html = re.sub(orfao_pattern, '\n', html, flags=re.DOTALL)

    with open(path, 'w', encoding='utf-8') as f:
        f.write(html)
    print(f"  {path}: shell removido")
    return True

if __name__ == '__main__':
    for p in sys.argv[1:]:
        strip_shell(p)
