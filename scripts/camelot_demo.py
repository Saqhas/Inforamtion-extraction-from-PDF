import camelot
output_camelot = camelot.read_pdf(
    filepath="data/input.pdf", pages=str(0), flavor="stream"
)
print(output_camelot)
table = output_camelot[0]
print(table)
print(table.parsing_report)
