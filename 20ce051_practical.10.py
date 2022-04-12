# 20ce051
# kirtan mangukiya
# https://github.com/kirtanmangukiya/project.git

from reportlab.pdfgen.canvas import Canvas
from reportlab.lib.units import inch, cm
canvas = Canvas("Result.pdf", pagesize=(8.5 * inch, 11 * inch))
canvas.setFont("Times-Roman", 28)
#canvas = Canvas("Result.pdf")
canvas.drawString(70, 695, "Charotar University Of Science &Technology")
canvas.drawString(155, 665, "3rd Semester Grade Report")
canvas.setFont("Times-Roman", 18)
canvas.drawString(80, 640, "Name: KIRTAN MANGUKIYA")
canvas.drawString(400, 640, "ID: 20CE051")
canvas.setFont("Times-Roman", 14)
canvas.drawString(180, 600, "Course")
canvas.drawString(400, 600, "Grade")
canvas.drawString(80, 560, "CE251 Java Programming")
canvas.drawString(400,560,"AA")
canvas.drawString(400,540,"AA")
canvas.drawString(80, 520, "CE252 Digital Electronics")
canvas.drawString(400,520,"AB")
canvas.drawString(400,500,"BC")
canvas.drawString(80, 480, "CE257 Data Communication & Networking")
canvas.drawString(400,480,"AA")
canvas.drawString(400,460,"AA")
canvas.drawString(80, 440, "MA253 Discrete Mathematics & Algebra ")
canvas.drawString(400,440,"AA")
canvas.drawString(80,380,"SGPA:")
canvas.drawString(120,380,"9.75")
canvas.drawString(80,350,"CGPA:")
canvas.drawString(120,350,"8.74")
canvas.save()