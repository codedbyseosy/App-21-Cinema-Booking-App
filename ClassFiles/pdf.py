import os
import webbrowser
from fpdf import FPDF
import random
import string


class PdfReport:
    """
    Creates a Pdf file that contains data about
    the flatmates such as their names, their
    due amount and the period of the bill.
    """
    def __init__(self, name, seat_id, price):
        self.name = name
        self.seat_id = seat_id
        self.price = str(price)  # Convert price to string

    @staticmethod
    def ticket_id(length):
        # Define the possible characters that can be used in the string
        characters = string.ascii_letters + string.digits  # Only letters and numbers
        # Generate the random string
        random_string = ''.join(random.choice(characters) for _ in range(length))
        return random_string

    def generate(self):
        # Create a PDF object
        pdf = FPDF(orientation='P', unit='pt', format='A4')
        pdf.add_page()

        # Insert title
        pdf.set_font(family='Times', size=24, style='B')
        pdf.cell(w=0, h=88, txt="Cinema Receipt", border=1, align="C", ln=1)

        # Insert name
        pdf.set_font(family='Times', size=14, style='B')
        pdf.cell(w=100, h=25, txt="Name: ", border=1)
        pdf.set_font(family='Times', size=14, style='B')
        pdf.cell(w=0, h=25, txt=self.name, border=1, ln=1)
        pdf.cell(w=0, h=5, txt="", border=0, ln=1)

        # Insert ticket ID
        pdf.set_font(family='Times', size=14, style='B')
        pdf.cell(w=100, h=25, txt="Ticket ID: ", border=1)
        pdf.set_font(family='Times', size=14, style='B')
        pdf.cell(w=0, h=25, txt=PdfReport.ticket_id(length=8), border=1, ln=1)
        pdf.cell(w=0, h=5, txt="", border=0, ln=1)

        # Insert seat purchased
        pdf.set_font(family='Times', size=14, style='B')
        pdf.cell(w=100, h=25, txt="Seat ID: ", border=1)
        pdf.set_font(family='Times', size=14, style='B')
        pdf.cell(w=0, h=25, txt=self.seat_id, border=1, ln=1)
        pdf.cell(w=0, h=5, txt="", border=0, ln=1)

        # Insert price
        pdf.set_font(family='Times', size=14, style='B')
        pdf.cell(w=100, h=25, txt="Price: ", border=1)
        pdf.set_font(family='Times', size=14, style='B')
        pdf.cell(w=0, h=25, txt=self.price, border=1, ln=1)
        pdf.cell(w=0, h=5, txt="", border=0, ln=1)

        # Save the PDF to a file
        pdf.output("Files/Generated Receipts/new_receipt.pdf")

        # Open the PDF file in a web browser
        webbrowser.open('file://' + os.path.realpath("Files/Generated Receipts/new_receipt.pdf"))
