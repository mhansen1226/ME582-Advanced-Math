export PYTHONPATH="${PYTHONPATH}:/Users/matthansen/Documents/Purdue/Classes/2026 Spring/MA528 - Advanced Math for Engineers II/Homework/HW12/lib"
MD_FILE="assignment.md"
PDF_FILE="${MD_FILE%.md}.pdf"

for file in scripts/*.py; do
    echo "Executing $file..."
    python3 "$file"
done

echo "Building PDF ..."
pandoc "$MD_FILE" -o "$PDF_FILE"
open "$PDF_FILE"
