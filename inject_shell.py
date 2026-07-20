# -*- coding: utf-8 -*-
"""
inject_shell.py — injeta cabeçalho/sidebar/breadcrumb/anterior-próximo
em todos os arquivos de conteúdo do ClinicusMed, a partir do catalogo.json.

Seguro pra rodar de novo no futuro (idempotente): sempre parte dos arquivos
como estão no repositório — se precisar reprocessar, reverta pro commit
anterior à injeção antes de rodar de novo, ou rode so nos arquivos novos.

Uso:
    python3 inject_shell.py                  # roda em tudo
    python3 inject_shell.py --dry-run         # so mostra o que faria
    python3 inject_shell.py --only ARQUIVO    # roda so num arquivo (teste)
"""
import json, re, os, sys, argparse

REPO = '/home/claude/resumos-clinicus'
CATALOGO_PATH = os.path.join(REPO, 'catalogo.json')
ETAPA_ORDEM = ['P1', 'P2', 'Final']
CSS_HREF = '/assets/shell-nav.css'
CATALOGO_HREF = '/index.html#catalogo'

def slugify(s):
    import unicodedata
    s = unicodedata.normalize('NFD', s.lower())
    s = ''.join(c for c in s if unicodedata.category(c) != 'Mn')
    s = re.sub(r'[^a-z0-9]+', '-', s).strip('-')
    return s

def parse_arquivo_field(raw, tipo, materia_nome):
    """Espelha parseEntry()/split do index.html: retorna lista de {path, label}."""
    if not raw:
        return []
    itens = []
    partes = [p.strip() for p in raw.split('|') if p.strip()]
    for i, arq in enumerate(partes):
        if '::' in arq:
            label, path = arq.split('::', 1)
            label, path = label.strip(), path.strip()
        else:
            prefixo = 'Guia de Estudo' if tipo == 'resumo' else 'Simulado'
            label = prefixo + ' - ' + materia_nome + (f' (parte {i+1})' if i > 0 else '')
            path = arq.strip()
        if path.lower().endswith('.pdf'):
            continue  # PDFs nao recebem o shell (nao sao HTML)
        itens.append({'path': path, 'label': label})
    return itens

def build_sequence(materia, sem_nome):
    """Retorna lista ordenada de itens (path, label, etapa) pra uma materia,
    seguindo P1->P2->Final, e dentro de cada etapa: resumo depois simulado."""
    seq = []
    for etapa_nome in ETAPA_ORDEM:
        etapa = materia['etapas'].get(etapa_nome)
        if not etapa or not etapa.get('disponivel'):
            continue
        for tipo in ('resumo', 'simulado'):
            bloco = etapa.get(tipo) or {}
            if not bloco.get('disponivel') or not bloco.get('arquivo'):
                continue
            itens = parse_arquivo_field(bloco['arquivo'], tipo, materia['nome'])
            for it in itens:
                seq.append({
                    'path': it['path'],
                    'label': it['label'],
                    'etapa': etapa_nome,
                    'tipo': 'Guia de Estudo' if tipo == 'resumo' else 'Simulado',
                    'materia': materia['nome'],
                    'semestre': sem_nome,
                })
    return seq

def esc(s):
    return (s.replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;').replace('"', '&quot;'))

def build_sidebar_html(seq, current_path):
    by_etapa = {}
    for it in seq:
        by_etapa.setdefault(it['etapa'], []).append(it)
    parts = [f'<p class="cmed-nav-sidebar-title">{esc(seq[0]["materia"])}</p>']
    for etapa_nome in ETAPA_ORDEM:
        if etapa_nome not in by_etapa:
            continue
        parts.append(f'<h4>{etapa_nome}</h4>')
        for it in by_etapa[etapa_nome]:
            is_current = (it['path'] == current_path)
            cls = 'cmed-nav-item is-current' if is_current else 'cmed-nav-item'
            ico = '📋' if it['tipo'] == 'Guia de Estudo' else '📝'
            href = '/' + it['path']
            parts.append(f'<a class="{cls}" href="{href}"><span class="ico">{ico}</span><span>{esc(it["label"])}</span></a>')
    return '\n    '.join(parts)

def build_header(back_href):
    return f'''<header class="cmed-nav-header">
  <a class="cmed-nav-brand" href="{back_href}"><img src="/assets/logo-header.png" alt="ClinicusMed"><span>ClinicusMed</span></a>
  <a class="cmed-nav-back" href="{back_href}">← Voltar para o Catálogo</a>
</header>'''

def build_breadcrumb(item):
    return f'''<nav class="cmed-nav-breadcrumb">
  <a href="{CATALOGO_HREF}">Início</a><span class="sep">›</span>
  <a href="{CATALOGO_HREF}">{esc(item['materia'])}</a><span class="sep">›</span>
  <span>{item['etapa']}</span><span class="sep">›</span>
  <span class="current">{esc(item['tipo'])}</span>
</nav>'''

def build_progress(idx, total):
    pct = round(((idx + 1) / total) * 100) if total else 0
    return f'''<div class="cmed-nav-progress-wrap">
  <div class="cmed-nav-progress-label"><span>Progresso em {{}}</span><span>{idx+1} de {total}</span></div>
  <div class="cmed-nav-progress-track"><div class="cmed-nav-progress-fill" style="width:{pct}%"></div></div>
</div>'''.format('')

def build_prevnext(prev_item, next_item):
    if prev_item:
        prev_html = f'''<a class="cmed-nav-pn-btn prev" href="/{prev_item['path']}">
    <span class="cmed-nav-pn-label">← Anterior</span>
    <span class="cmed-nav-pn-title">{esc(prev_item['label'])}</span>
  </a>'''
    else:
        prev_html = '<span class="cmed-nav-pn-btn prev disabled"><span class="cmed-nav-pn-label">← Anterior</span><span class="cmed-nav-pn-title">Início da disciplina</span></span>'

    if next_item:
        next_html = f'''<a class="cmed-nav-pn-btn next" href="/{next_item['path']}">
    <span class="cmed-nav-pn-label">Próximo →</span>
    <span class="cmed-nav-pn-title">{esc(next_item['label'])}</span>
  </a>'''
    else:
        next_html = '<span class="cmed-nav-pn-btn next disabled"><span class="cmed-nav-pn-label">Próximo →</span><span class="cmed-nav-pn-title">Fim da disciplina 🎉</span></span>'

    return f'<nav class="cmed-nav-prevnext">\n  {prev_html}\n  {next_html}\n</nav>'

MOBILE_TOGGLE_SCRIPT = '''<script>
(function(){
  var sb = document.querySelector('.cmed-nav-sidebar');
  var btn = document.querySelector('.cmed-nav-sidebar-toggle');
  if(btn){ btn.onclick = function(){ sb.classList.toggle('is-open'); }; }
  // marca este item como "visto" no localStorage (progresso simples, sem backend)
  try{
    var key = 'cmed_visto_' + location.pathname;
    localStorage.setItem(key, '1');
  }catch(e){}
})();
</script>
<script>
(function(){
  var KEY = 'cmed_reading_mode';
  var SEEN_KEY = 'cmed_reading_mode_seen_intro';
  var html = document.documentElement;
  var btn = document.getElementById('cmedReadingBtn');
  try{
    var stored = localStorage.getItem(KEY);
    var seenIntro = localStorage.getItem(SEEN_KEY);
    if(stored === '1'){
      html.classList.add('cmed-reading-mode');
    } else if(stored === null && seenIntro === '1'){
      // aluno ja navegou antes mas nunca mexeu no toggle -> assume preferencia por modo leitura
      html.classList.add('cmed-reading-mode');
    }
    if(!seenIntro){ localStorage.setItem(SEEN_KEY, '1'); }
  }catch(e){}
  if(btn){
    btn.onclick = function(){
      html.classList.toggle('cmed-reading-mode');
      try{ localStorage.setItem(KEY, html.classList.contains('cmed-reading-mode') ? '1' : '0'); }catch(e){}
    };
  }
})();
</script>'''

READING_MODE_BTN = '''<button class="cmed-reading-btn" id="cmedReadingBtn">
  <span class="cmed-reading-label-enter">⛶ Modo Leitura</span>
  <span class="cmed-reading-label-exit">✕ Sair do Modo Leitura</span>
</button>'''

def fix_body_flex_grid_conflict(html):
    """Se o arquivo define body{display:flex/grid} pro layout proprio dele,
    retargeta pra .cmed-nav-main - senao o body flex/grid do arquivo
    'puxa' nosso cabecalho/breadcrumb/sidebar pro lugar errado tambem."""
    m = re.search(r'\bbody\s*\{[^}]*display\s*:\s*(flex|grid)[^}]*\}', html)
    if not m:
        return html
    regra_original = m.group(0)
    regra_nova = re.sub(r'^body\s*\{', '.cmed-nav-main{', regra_original)
    return html.replace(regra_original, regra_nova, 1)


def inject_file(item, seq, idx, dry_run=False):
    full_path = os.path.join(REPO, item['path'])
    if not os.path.exists(full_path):
        print(f"  ⚠️  arquivo nao encontrado, pulando: {item['path']}")
        return False

    with open(full_path, encoding='utf-8') as f:
        html = f.read()

    if 'cmed-nav-header' in html:
        print(f"  ⏭️  ja tem o shell injetado, pulando: {item['path']}")
        return False

    # corrige conflito de layout ANTES de injetar (ver funcao acima)
    html = fix_body_flex_grid_conflict(html)

    # 1. injeta o <link> do CSS no <head>
    if '</head>' not in html:
        print(f"  ⚠️  sem </head>, pulando: {item['path']}")
        return False
    html = html.replace('</head>', f'<link rel="stylesheet" href="{CSS_HREF}">\n</head>', 1)

    # 2. monta os blocos
    back_href = CATALOGO_HREF
    header_html = build_header(back_href)
    breadcrumb_html = build_breadcrumb(item)
    progress_html = build_progress(idx, len(seq)).replace(
        'Progresso em ', f'Progresso em {esc(item["materia"])}'
    )
    sidebar_html = build_sidebar_html(seq, item['path'])
    prev_item = seq[idx - 1] if idx > 0 else None
    next_item = seq[idx + 1] if idx < len(seq) - 1 else None
    prevnext_html = build_prevnext(prev_item, next_item)

    top_block = f'''{READING_MODE_BTN}
{header_html}
{breadcrumb_html}
{progress_html}
<div class="cmed-nav-layout">
  <aside class="cmed-nav-sidebar">
    <button class="cmed-nav-sidebar-toggle">☰ Navegação da disciplina <span>▾</span></button>
    <div class="cmed-nav-sidebar-list">
    {sidebar_html}
    </div>
  </aside>
  <div class="cmed-nav-main">
'''
    bottom_block = f'''
  </div>
</div>
{prevnext_html}
{MOBILE_TOGGLE_SCRIPT}
'''

    # 3. injeta logo apos <body> e antes de </body>
    if '<body>' not in html or '</body>' not in html:
        print(f"  ⚠️  <body> nao encontrado no formato esperado, pulando: {item['path']}")
        return False

    html = html.replace('<body>', '<body>\n' + top_block, 1)
    # ultima ocorrencia de </body>
    last_idx = html.rfind('</body>')
    html = html[:last_idx] + bottom_block + html[last_idx:]

    if dry_run:
        print(f"  [dry-run] injetaria em: {item['path']} (prev={'sim' if prev_item else 'nao'}, next={'sim' if next_item else 'nao'})")
        return True

    with open(full_path, 'w', encoding='utf-8') as f:
        f.write(html)
    print(f"  ✅ {item['path']}")
    return True


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--dry-run', action='store_true')
    parser.add_argument('--only', default=None, help='processa so esse path (teste)')
    args = parser.parse_args()

    with open(CATALOGO_PATH, encoding='utf-8') as f:
        catalogo = json.load(f)

    total_injetados = 0
    total_pulados = 0
    seen_paths = set()

    for sem in catalogo['semestres']:
        for materia in sem['materias']:
            seq = build_sequence(materia, sem.get('nome', ''))
            if not seq:
                continue
            print(f"\n=== {materia['nome']} ({len(seq)} itens) ===")
            for idx, item in enumerate(seq):
                if item['path'] in seen_paths:
                    continue  # evita reprocessar o mesmo arquivo fisico 2x
                if args.only and item['path'] != args.only:
                    continue
                seen_paths.add(item['path'])
                ok = inject_file(item, seq, idx, dry_run=args.dry_run)
                if ok:
                    total_injetados += 1
                else:
                    total_pulados += 1

    print(f"\n{'='*60}")
    print(f"Total injetados: {total_injetados} | pulados/ja feitos: {total_pulados}")

if __name__ == '__main__':
    main()
