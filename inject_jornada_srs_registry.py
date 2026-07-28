# -*- coding: utf-8 -*-
"""
inject_jornada_srs_registry.py — injeta um script leve que registra, num
indice compartilhado no localStorage, o ID de flashcards (CHAPTER_ID) de
cada capitulo que os visualiza. Isso permite que /jornada/ calcule
"sugestao de revisao" olhando os capitulos que o aluno ja visitou.

So funciona em capitulos que tem a variavel CHAPTER_ID declarada (padrao
usado nos capitulos com flashcards SM-2). Simulados e capitulos sem
flashcards sao ignorados automaticamente (checagem em tempo de execucao
no navegador, nao em tempo de injecao).

Uso:
    python3 inject_jornada_srs_registry.py
    python3 inject_jornada_srs_registry.py --dry-run
    python3 inject_jornada_srs_registry.py --only ARQUIVO
"""
import json, os, argparse

REPO = '/home/claude/resumos-clinicus'
CATALOGO_PATH = os.path.join(REPO, 'catalogo.json')
ETAPA_ORDEM = ['P1', 'P2', 'Final']
MARKER = 'clinicus_jornada_srs_registry'

def parse_arquivo_field(raw, tipo, materia_nome):
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
            continue
        itens.append({'path': path, 'label': label})
    return itens

def esc_js(s):
    return s.replace('\\', '\\\\').replace("'", "\\'")

def build_items():
    with open(CATALOGO_PATH, encoding='utf-8') as f:
        data = json.load(f)
    items = []
    for sem in data['semestres']:
        for materia in sem['materias']:
            for etapa_nome in ETAPA_ORDEM:
                etapa = materia['etapas'].get(etapa_nome)
                if not etapa or not etapa.get('disponivel'):
                    continue
                bloco = (etapa.get('resumo') or {})
                if not bloco.get('disponivel') or not bloco.get('arquivo'):
                    continue
                for it in parse_arquivo_field(bloco['arquivo'], 'resumo', materia['nome']):
                    items.append({'path': it['path'], 'label': it['label'], 'materia': materia['nome']})
    return items

def build_script(item):
    return f'''<script>
try{{
  if(typeof CHAPTER_ID !== 'undefined'){{
    var srsReg = JSON.parse(localStorage.getItem('{MARKER}') || '[]');
    var srsKey = 'clinicus_srs_' + CHAPTER_ID;
    var entry = {{ materia: '{esc_js(item["materia"])}', titulo: '{esc_js(item["label"])}', url: location.pathname, srsKey: srsKey }};
    srsReg = srsReg.filter(function(e){{ return e.srsKey !== srsKey; }});
    srsReg.push(entry);
    localStorage.setItem('{MARKER}', JSON.stringify(srsReg));
  }}
}}catch(e){{}}
</script>'''

def inject_file(item, dry_run=False):
    full_path = os.path.join(REPO, item['path'])
    if not os.path.exists(full_path):
        print(f"  ⚠️  arquivo nao encontrado, pulando: {item['path']}")
        return False
    with open(full_path, encoding='utf-8') as f:
        html = f.read()
    if MARKER in html:
        print(f"  ⏭️  ja tem registro srs, pulando: {item['path']}")
        return False
    if '</body>' not in html:
        print(f"  ⚠️  sem </body>, pulando: {item['path']}")
        return False
    script = build_script(item)
    last_idx = html.rfind('</body>')
    html = html[:last_idx] + script + '\n' + html[last_idx:]
    if dry_run:
        print(f"  [dry-run] injetaria srs-registry em: {item['path']}")
        return True
    with open(full_path, 'w', encoding='utf-8') as f:
        f.write(html)
    print(f"  ✅ {item['path']}")
    return True

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--dry-run', action='store_true')
    parser.add_argument('--only', default=None)
    args = parser.parse_args()
    items = build_items()
    if args.only:
        items = [it for it in items if it['path'] == args.only]
    print(f"Total de itens a processar: {len(items)}")
    ok = 0
    for it in items:
        if inject_file(it, dry_run=args.dry_run):
            ok += 1
    print(f"\\nConcluido: {ok}/{len(items)} arquivos processados.")

if __name__ == '__main__':
    main()
