#!/usr/bin/env python3
"""
Injeta a secao "Complemento em Video" (aba p2) em capitulos ClinicusMed.
- Adiciona o botao de aba "Vídeo" no nav.tabs, entre Casos Clinicos(p1) e Flashcards(p3)
- Adiciona a <section id="p2"> com o loader que busca /videos.json por CHAPTER_ID
- Idempotente: se ja injetado (marcador CMED-VIDEO-SECTION), pula o arquivo
- Nao precisa ser re-executado ao trocar videos: o conteudo e' buscado em runtime

Uso:
  python3 inject_video_section.py                # roda em todos os capitulos com CHAPTER_ID
  python3 inject_video_section.py --only "path"   # roda so num arquivo
  python3 inject_video_section.py --dry-run       # so lista o que faria
"""
import argparse
import re
import sys
from pathlib import Path

ROOT = Path(__file__).parent
TEMPLATE_PATH = Path("/home/claude/cmed_scripts/video_section_template.html")

MARKER = "CMED-VIDEO-SECTION"

NAV_BTN = '  <button data-p="p2">🎥 Vídeo</button>\n'


def find_chapter_files():
    """Encontra todo HTML que tem CHAPTER_ID definido (capitulos no padrao novo)."""
    files = []
    for p in ROOT.rglob("*.html"):
        if "/mnt/" in str(p):
            continue
        try:
            text = p.read_text(encoding="utf-8", errors="ignore")
        except Exception:
            continue
        if "const CHAPTER_ID" in text and 'data-p="p1"' in text and 'data-p="p3"' in text:
            files.append(p)
    return files


def inject_one(path: Path, template: str, dry_run: bool) -> str:
    text = path.read_text(encoding="utf-8")

    if MARKER in text:
        return "skip-ja-injetado"

    # 1) Inserir botao de aba entre p1 e p3
    nav_pattern = re.compile(r'(  <button data-p="p1">[^<]*</button>\n)(  <button data-p="p3">)')
    if not nav_pattern.search(text):
        return "erro-nav-nao-encontrado"
    new_text = nav_pattern.sub(lambda m: m.group(1) + NAV_BTN + m.group(2), text, count=1)

    # 2) Inserir a secao p2 (com style+html+script) logo apos o fechamento da secao p1,
    #    antes do comentario/abertura da secao p3 (Flashcards)
    section_p1_close_pattern = re.compile(
        r'(<section class="panel" id="p1">.*?</section>\s*\n)(\s*<!-- =+ FLASHCARDS =+ -->\s*\n<section class="panel" id="p3">)',
        re.S,
    )
    m = section_p1_close_pattern.search(new_text)
    if not m:
        return "erro-secao-p1-nao-encontrada"

    injected_block = template + "\n\n"
    new_text = section_p1_close_pattern.sub(
        lambda mm: mm.group(1) + injected_block + mm.group(2), new_text, count=1
    )

    if dry_run:
        return "ok(dry-run)"

    path.write_text(new_text, encoding="utf-8")
    return "ok"


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--only", help="processa so esse arquivo (caminho relativo)")
    ap.add_argument("--dry-run", action="store_true")
    args = ap.parse_args()

    template = TEMPLATE_PATH.read_text(encoding="utf-8")

    if args.only:
        targets = [ROOT / args.only]
    else:
        targets = find_chapter_files()

    print(f"Total de itens a processar: {len(targets)}")
    results = {}
    for p in targets:
        if not p.exists():
            print(f"  ⚠️  nao encontrado: {p}")
            continue
        status = inject_one(p, template, args.dry_run)
        results.setdefault(status, []).append(p)
        rel = p.relative_to(ROOT)
        icon = "✅" if status.startswith("ok") else ("⏭️ " if status.startswith("skip") else "❌")
        print(f"  {icon} {rel} [{status}]")

    print("\nResumo:")
    for status, items in results.items():
        print(f"  {status}: {len(items)}")


if __name__ == "__main__":
    main()
