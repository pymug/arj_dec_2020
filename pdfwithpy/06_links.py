# https://github.com/youtubetotaltechnology/source
from reportlab.pdfgen import canvas
pdf=canvas.Canvas("output/06.pdf")
pdf.drawCentredString(50,100,"with bookmark")
pdf.bookmarkPage("page1")
pdf.addOutlineEntry("page1 for bookmark","page1")
pdf.showPage()
pdf.drawCentredString(10,100,"with bookmark")
pdf.bookmarkPage("page2")
pdf.addOutlineEntry("page1 for bookmark","page2")
pdf.save()