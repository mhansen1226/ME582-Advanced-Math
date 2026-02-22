MD_FILE="assignment.md"
PDF_FILE="${MD_FILE%.md}.pdf"

echo "Running python scripts ..."
python3 scripts/13.3.1.py
python3 scripts/13.3.3.py
python3 scripts/13.3.5.py
python3 scripts/13.3.7.py
python3 scripts/13.5.19.py

echo "Building PDF ..."
pandoc "$MD_FILE" -o "$PDF_FILE"
open "$PDF_FILE"
