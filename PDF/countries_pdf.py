from fpdf import FPDF
import csv

with open("countries.txt", encoding="utf8") as csv_file:
    data = list(csv.reader(csv_file, delimiter=","))

pdf = FPDF()
pdf.set_font("helvetica", size=14)


pdf.add_page()
with pdf.table(
    borders_layout="NO_HORIZONTAL_LINES",
    cell_fill_color=(224, 235, 255),
    col_widths=(42, 39, 35, 42),
    line_hight=6,
    text_align=("LEFT", "CENTER", "RIGHT", "RIGHT"),
    width=160
) as table:
    for data_row in data:
        row = table.row()
        for datum in data_row:
            row.cell(datum)

pdf.output("table.pdf")
