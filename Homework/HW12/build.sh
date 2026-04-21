MD_FILE="assignment.md"
PDF_FILE="${MD_FILE%.md}.pdf"

# for file in scripts/*.py; do
#     echo "Executing $file..."
#     python3 "$file"
# done

echo "Building PDF ..."
pandoc "$MD_FILE" -o "$PDF_FILE"
open "$PDF_FILE"
