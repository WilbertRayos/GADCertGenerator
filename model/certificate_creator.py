
from reportlab.lib.pagesizes import A4, landscape
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
from reportlab.platypus import (Flowable, Paragraph,
                                SimpleDocTemplate, Spacer)
from reportlab.lib.enums import TA_CENTER

from reportlab.lib.utils import ImageReader


class GenerateBackground(Flowable):
    def __int__(self):
        Flowable.__init__(self)

    def draw(self):
        self.background = ImageReader("img/background.png")
        self.canv.drawImage(self.background, -78, -517, width=11.7*inch, height=8.3*inch)


class NTCHeader(Flowable):

    def __init__(self):
        Flowable.__init__(self)
        self.logo = ImageReader("img/ntc.png")

    def draw(self):
        self.canv.setFont("Helvetica-Bold", 22)
        self.canv.drawImage(self.logo, 20, -40, height=1*inch, width=1*inch, mask="auto")
        self.canv.drawString(1.7*inch, 0.05*inch, "REPUBLIC OF THE PHILIPPINES")
        self.canv.line(122, -5, 655, 0)
        self.canv.drawString(1.7*inch, -0.35*inch, "NATIONAL TELECOMMUNICATIONS COMMISSION")


class CertificateSignatory(Flowable):

    def __init__(self):
        Flowable.__init__(self)

    def draw(self):
        self.canv.setFont("Helvetica-Bold", 16)
        self.canv.drawString(3.1*inch, -6*inch, "HON. GAMALIEL A. CORDOBA")
        self.canv.setFont("Helvetica", 16)
        self.canv.drawString(4.1*inch, -6.3*inch, "Commissioner")

class CertificateCreator:

    def __init__(self, name, sex, title, date):

        story=[]
        doc = SimpleDocTemplate("meme.pdf",pagesize=landscape(A4))
        styles=getSampleStyleSheet()
        styles_content = ParagraphStyle('style_center', fontName="Helvetica", fontSize=14, parent=styles['Normal'], alignment=TA_CENTER, leading=24)
        styles_emphasize = ParagraphStyle('styles_emphasize', fontName="Helvetica-bold",parent=styles['Normal'], fontSize=28, alignment=TA_CENTER, leading=30)
        story.append(GenerateBackground())
        story.append(NTCHeader())
        story.append(CertificateSignatory())
        story.append(Spacer(0, 1 * inch))
        ptext = '<span>%s</span>' % "This"
        story.append(Paragraph(ptext, styles_content))
        ptext = '<span>%s</span>' % "Certificate of Appreciation"
        story.append(Paragraph(ptext, styles_emphasize))
        story.append(Spacer(0, 0.1*inch))
        ptext = '<span>%s</span>' % "is hereby given to"
        story.append(Paragraph(ptext, styles_content))
        ptext = '<span>%s</span>' % name
        story.append(Paragraph(ptext, styles_emphasize))
        story.append(Spacer(0, 0.1*inch))
        ptext = '<span>%s</span>' % f"In grateful recognition and sincere appreciation of {'his' if sex == 'Male' else 'her'} invaluable service rendered as Resource Speaker in the"
        story.append(Paragraph(ptext, styles_content))
        ptext = '<span>%s</span>' % title
        story.append(Paragraph(ptext, styles_emphasize))
        story.append(Spacer(0, 0.2 * inch))
        ptext = '<span>%s</span>' % f"held on {date} at the NTC Building, BIR Road, East Triangle, Diliman, Quezon City via ZOOM Video Conferencing"
        story.append(Paragraph(ptext, styles_content))

        doc.build(story)