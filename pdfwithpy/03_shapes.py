
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
from reportlab.lib.colors import PCMYKColor, PCMYKColorSep, Color, black, blue, red
from math import sin 
from math import cos
HEIGHT = A4[1]
WIDTH = A4[0]
c = canvas.Canvas("output/03.pdf", pagesize=A4)
c.setLineWidth(.3)

c.line(40, 40, 40, HEIGHT-40)
c.line(40, 40, WIDTH-40, 40)
c.setFillColorRGB(0, 0, 255)
c.setStrokeColor(Color(0, 255, 0))
c.line(0, 100, WIDTH, 100)
c.line(100, 0, 100, HEIGHT)
c.setStrokeColor(Color( 0, 0, 0, alpha=0))
c.ellipse(100, 100, 50, 50, fill=1)

c.setFillColor(Color( 0, 255, 100))
for i in range(50, int(HEIGHT-50), 10):
    c.circle(200 + sin(i) * 5, i, 2, fill=1)

for i in range(50, int(HEIGHT-50), 5):
    c.circle(250 + sin(i) * 5, i, 2, fill=1)

for i in range(50, int(HEIGHT-50), 10):
    c.circle(300 + sin(i) * 5, i, 2, fill=1)

for i in range(50, int(HEIGHT-50), 5):

    r = ((int(HEIGHT-50)-i)//10)
    x_coord = 350 + sin(i) * r
    c.circle(x_coord, HEIGHT-i, 5, fill=1)

c.save()