MD_FILE="assignment.md"
PDF_FILE="${MD_FILE%.md}.pdf"

python3 scripts/poles.py

echo "Building PDF ..."
pandoc "$MD_FILE" -o "$PDF_FILE"
open "$PDF_FILE"
