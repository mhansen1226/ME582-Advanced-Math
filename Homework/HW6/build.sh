MD_FILE="assignment.md"
PDF_FILE="${MD_FILE%.md}.pdf"

# python3 scripts/13.7.15.py

echo "Building PDF ..."
pandoc "$MD_FILE" -o "$PDF_FILE"
open "$PDF_FILE"
