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

    # remove o bloco do topo: de <header class="cmed-nav-header"> ate <div class="cmed-nav-main">
    html = re.sub(
        r'<header class="cmed-nav-header">.*?<div class="cmed-nav-main">\n',
        '',
        html, count=1, flags=re.DOTALL
    )

    # remove o bloco do rodape: do fechamento do cmed-nav-main ate o fim do script de toggle mobile
    html = re.sub(
        r'\n  </div>\n</div>\n<nav class="cmed-nav-prevnext">.*?</script>\n',
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
