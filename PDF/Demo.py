from fpdf import FPDF


class PDF(FPDF):



pdf = FPDF()

pdf.add_page()
pdf.set_font("helvetica", "B", 16)
pdf.cell(40, 10, "Hello world")
pdf.output("sample.pdf")
