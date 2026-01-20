from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from reportlab.lib.utils import simpleSplit
import io

def create_pdf(text, subject):
    buffer = io.BytesIO()
    c = canvas.Canvas(buffer, pagesize=letter)
    width, height = letter
    
    # Header
    c.setFont("Helvetica-Bold", 16)
    c.drawCentredString(width/2, height - 50, f"PREDICTED BOARD PAPER 2026")
    c.setFont("Helvetica-Bold", 14)
    c.drawCentredString(width/2, height - 70, f"Subject: {subject}")
    c.line(50, height - 80, width - 50, height - 80)
    
    # Body Text
    c.setFont("Helvetica", 11)
    y_position = height - 100
    lines = text.split('\n')
    
    for line in lines:
        # Wrap text if it is too long for the page width
        wrapped_lines = simpleSplit(line, "Helvetica", 11, width - 100)
        for wrapped_line in wrapped_lines:
            if y_position < 50:  # Start a new page if we hit the bottom
                c.showPage()
                c.setFont("Helvetica", 11)
                y_position = height - 50
            c.drawString(50, y_position, wrapped_line)
            y_position -= 15
            
    c.save()
    buffer.seek(0)
    return buffer
