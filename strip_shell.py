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

    # remove o bloco do rodape: do fechamento do cmed-nav-main ate o fim do(s) script(s)
    # (arquivos antigos tem so 1 script de toggle mobile; novos tem 2: toggle mobile + modo leitura)
    html = re.sub(
        r'\n  </div>\n</div>\n<nav class="cmed-nav-prevnext">.*?</script>(?:\s*<script>.*?</script>)?\n',
        '\n',
        html, count=1, flags=re.DOTALL
    )

    with open(path, 'w', encoding='utf-8') as f:
        f.write(html)
    print(f"  {path}: shell removido")
    return True

if __name__ == '__main__':
    for p in sys.argv[1:]:
        strip_shell(p)
