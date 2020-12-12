from reportlab.lib.pagesizes import A4 # not a4
from reportlab.pdfgen import canvas
from math import sin
from reportlab.pdfbase.pdfmetrics import stringWidth

HEIGHT = A4[1]
WIDTH = A4[0]

canvas = canvas.Canvas("output/02.pdf", pagesize=A4)
canvas.setLineWidth(.3)
canvas.setFont('Helvetica', 50)
str1 = 'HAPPY MEETUP'
str1_width = stringWidth(str1, 'Helvetica', 50)
str2 = 'FOLKS'
str2_width = stringWidth(str2, 'Helvetica', 50)

canvas.drawString((WIDTH-str1_width)//2, HEIGHT//2 + 100, str1)
canvas.drawString((WIDTH-str2_width)//2, HEIGHT//2 - 100, str2)
canvas.setFillColorRGB(0, 100, 100)

canvas.setFont('Helvetica', 12)
for i in range(0, int(HEIGHT)):
    canvas.drawString(sin(i)*2,i*2,"❤")
for i in range(0, int(HEIGHT)):
    canvas.drawString(WIDTH-12+sin(i)*2, i*2,"❤")

canvas.save()


