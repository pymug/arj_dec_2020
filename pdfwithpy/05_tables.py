import json
from reportlab.platypus import Table
from reportlab.platypus import Image
from reportlab.platypus import TableStyle
from reportlab.lib import colors
from reportlab.platypus import SimpleDocTemplate
from reportlab.platypus import Paragraph
from reportlab.lib.pagesizes import letter
from reportlab.lib.pagesizes import A4
from reportlab.lib.pagesizes import landscape
from reportlab.platypus.flowables import Flowable
from reportlab.lib.units import inch
import time
from reportlab.lib.enums import TA_JUSTIFY
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Image
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
from reportlab.platypus import PageBreak



class verticalText(Flowable):

    '''Rotates a text in a table cell.'''
    def __init__(self, text):
        Flowable.__init__(self)
        self.text = text

    def draw(self):
        canvas = self.canv
        canvas.rotate(90)
        fs = canvas._fontsize
        canvas.translate(1, -fs/1.2)  # canvas._leading?
        canvas.setFont('Helvetica-Bold', 8)
        canvas.drawString(0, 0, self.text)

    def wrap(self, aW, aH):
        canv = self.canv
        fn, fs = canv._fontname, canv._fontsize
        return canv._leading, 1 + canv.stringWidth(self.text, fn, fs)


outpdfpath = 'output/05.pdf'
pdf = SimpleDocTemplate(outpdfpath, pagesize=landscape(A4), rightMargin=15,leftMargin=15,
                        topMargin=72,bottomMargin=18)
pdf.title = 'Class Report'

cols = ['Name', 'Age', 'Address']
cols = [verticalText(t) for t in cols]

data= [
    ['', '', ''],
    ['', '', ''],
    ['', '', ''],
    ['', '', ''],
    ['', '', ''],
    ['', '', ''],
    ['', '', ''],
    ['', '', ''],
    ['', '', ''],
]
data.insert(0, cols)
t=Table(data)
t.setStyle(TableStyle([
        ('LINEBEFORE',(0,0),(-1, -1),1,colors.HexColor('#808080')),
    ]))
t.setStyle(TableStyle([
        ('LINEAFTER',(-1, 0),(-1, -1),0.5, colors.HexColor('#808080')),
        ('FONTSIZE', (0, 0),(-1, -1), 7),
    ]))
rowNumb = len(data)
for i in range(1, rowNumb):
    if i % 2 == 0:
        bc = colors.white
    else:
        bc = colors.HexColor('#f2f2f2')
    
    ts = TableStyle(
        [('BACKGROUND', (0,i),(-1,i), bc)]
    )
    t.setStyle(ts)
styles=getSampleStyleSheet()
styles.add(ParagraphStyle(name='Justify', alignment=TA_JUSTIFY))
title_style = styles['Heading1']
title_style.alignment = 1
elems = []
ptext = '<font size="9">{}</font>'.format('rgferg')

title = '{} {} {} - Semester {} {}'.format('Grade7', 'Boys', 'A', 
    2, 2020)

elems.append(Paragraph(title, title_style)) 
elems.append(Spacer(1, 23))
elems.append(t)
pdf.build(elems)
    