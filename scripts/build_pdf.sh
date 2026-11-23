#!/usr/bin/env bash
# Builds build/kill_team_podrecznik.pdf from podrecznik/*.md (preview only, not the source of truth).
# Requires: pandoc, wkhtmltopdf. Run from repo root: ./scripts/build_pdf.sh
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
SRC="$ROOT/podrecznik"
OUT="$ROOT/build"
TMP="$(mktemp -d)"
mkdir -p "$OUT"

ORDER=(README 01_zasady_podstawowe 02_misje 03_sprzet 04_strefy_walki 05_inne_tryby_gry 06_slowniczek 07_oddzialy/README)
for f in "$SRC"/07_oddzialy/*.md; do
  n="07_oddzialy/$(basename "$f" .md)"
  [[ "$n" == "07_oddzialy/README" ]] || ORDER+=("$n")
done

for f in "${ORDER[@]}"; do
  cat "$SRC/$f.md"
  printf '\n\n<div style="page-break-after: always;"></div>\n\n'
done | sed -E 's#!\[([^]]*)\]\(obrazki/ilustracje/[^)]*\)#*[Miejsce na ilustrację: \1]*#' > "$TMP/all.md"

pandoc "$TMP/all.md" -f gfm -t html5 -s --metadata pagetitle="Kill Team - Podrecznik" \
  -c "$ROOT/scripts/pdf_style.css" --resource-path="$SRC" --embed-resources -o "$TMP/all.html"
wkhtmltopdf --enable-local-file-access -q --encoding utf-8 -B 15 -T 15 -L 15 -R 15 \
  "$TMP/all.html" "$OUT/kill_team_podrecznik.pdf"
echo "Built $OUT/kill_team_podrecznik.pdf"
