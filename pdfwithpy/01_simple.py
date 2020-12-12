from reportlab.lib.pagesizes import A4 # not a4
from reportlab.pdfgen import canvas

# Demo
canvas = canvas.Canvas("output/01.pdf", pagesize=A4)
canvas.setLineWidth(.3)
canvas.setFont('Helvetica', 12)
canvas.drawString(0,0,'Boring Font')

canvas.save()
