from fpdf import FPDF

pdf = FPDF()

pdf.add_page()
pdf.set_font("Helvetica", size=20)
pdf.write(5, "To find out what's new in tutorial, click")
pdf.set_font(style="U")
link = pdf.add_link(page=2)
