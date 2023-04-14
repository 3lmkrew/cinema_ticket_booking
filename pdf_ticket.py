import fpdf
import random
import pyqrcode

# Generates QR code with qr_code() function
# Generates a random ticket ID with ticket_id() function
# Generates a PDF ticket with users information
# Adds QR code and random ticket id to the PDF and saves copy under ticket_folder


def qr_code(link):
    """Generates QR code with website link you pass and returns .png image"""
    url = pyqrcode.create(link)
    png_ticket = url.png('images/digital_ticket.png', scale=6)
    return png_ticket


def ticket_id():
    """Will generate a random ID by choosing random letters/numbers from list"""
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
               'u',
               'v', 'w', 'x', 'y', 'z', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    random_id = [random.choice(letters) for num in range(1, 7)]
    random_id = "".join(random_id).capitalize()
    return random_id


class Ticket:
    """If ticket purchase is successful, will generate a PDF digital ticket with users data"""
    def __init__(self, id_seat, user_name, price, seat):
        self.id = id_seat
        self.user_name = user_name
        self.price = price
        self.seat = seat

    def to_pdf(self, path):
        qr_url = qr_code("https://github.com/3lmkrew")
        pdf = fpdf.FPDF()
        pdf.add_page()
        pdf.set_font(family='Arial', style='B', size=24)
        pdf.set_text_color(r=255, g=83, b=33)
        pdf.cell(w=0, h=20, txt="Cinema Movie Ticket", align="C", ln=1, border=1)
        pdf.set_text_color(r=0, g=0, b=0)
        pdf.set_font(family='Times', style='B', size=18)
        pdf.cell(w=0, h=15, txt=f"Ticket ID: {self.id}", align="L", ln=1, border=1)
        pdf.cell(w=0, h=5, txt="", border=0, ln=1)
        pdf.cell(w=0, h=15, txt=f"Ticket price: ${self.price}", align="L", ln=1, border=1)
        pdf.cell(w=0, h=5, txt="", border=0, ln=1)
        pdf.cell(w=0, h=15, txt=f'Seat number: {self.seat}', align="L", ln=1, border=1)
        pdf.cell(w=0, h=5, txt="", border=0, ln=1)
        pdf.cell(w=0, h=15, txt=f'Name: {self.user_name}', align="L", ln=1, border=1)
        pdf.image(name="images/ticket.png", x=165, y=12, w=15, h=15)
        pdf.image(name="images/ticket.png", x=30, y=12, w=15, h=15)
        pdf.image(name="images/digital_ticket.png", x=67, y=31, w=12, h=12)
        pdf.image(name="images/clapboard.png", x=80, y=148, w=50, h=50)
        pdf.cell(w=0, h=10, txt="", border=0, ln=1)
        pdf.cell(w=0, h=15, txt=f'Thank you for your purchase,', align="C", ln=2, border=0)
        pdf.cell(w=0, h=10, txt=f'{self.user_name}', align="C", ln=2, border=0)
        try:
            pdf.output(path)

        except PermissionError:
            print("Your PDF file is open, I was not able to create new ticket but:")
