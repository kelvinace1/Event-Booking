from reportlab.pdfgen import canvas
from io import BytesIO

def generate_ticket_pdf(booking):
    buffer = BytesIO()
    p = canvas.Canvas(buffer)

    
    p.drawString(100, 800, f'Ticket ID: {booking.id}')
    p.drawString(100, 780, f'Event: {booking.ticket.event}')
    p.drawString(100, 760, f'Ticket Type: {booking.ticket.ticket_type}')
    p.drawString(100, 740, f'Quantity: {booking.quantity}')
   

    p.showPage()
    p.save()

    buffer.seek(0)
    return buffer
