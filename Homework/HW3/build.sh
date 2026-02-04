MD_FILE="assignment.md"
PDF_FILE="${MD_FILE%.md}.pdf"

# echo Running python scripts ...
# python3 scripts/10.5.14.py
# python3 scripts/10.5.15.py
# python3 scripts/10.5.18.py

echo "Building PDF ..."
pandoc "$MD_FILE" -o "$PDF_FILE"
open "$PDF_FILE"
