import sqlite3
from ClassFiles.seat import Seat
from ClassFiles.balance import Balance
from ClassFiles.pdf import PdfReport


class Card:
    """Checks whether or not a user has entered
    their correct card details.
    """
    messages = {
        "purchase_successful": "Purchase was successful! Enjoy your movie.",
        "details_incorrect": "The card details you have entered are incorrect. "
                             "Please check your details or use another card.",
    }

    def __init__(self, name, seat_id, card_type, card_number, cvc, holder_name):
        self.name = name
        self.seat_id = seat_id
        self.card_type = card_type
        self.card_number = card_number
        self.cvc = cvc
        self.holder_name = holder_name

    def check_card_details(self):
        # Connect to the banking database to verify card details
        connection = sqlite3.connect('databases/banking.db')
        cursor = connection.cursor()
        cursor.execute("""SELECT * FROM Card WHERE type=? AND number=? AND cvc=? AND holder=?""",
                       (self.card_type, self.card_number, self.cvc, self.holder_name))
        user = cursor.fetchone()
        connection.close()

        if user is not None:
            # Check seat availability
            seat = Seat(seat_id=self.seat_id)
            result = seat.seat_availability()

            if result == "Purchase was successful! Enjoy your movie.":
                # Update balance and change seat availability
                balance = Balance(seat_id=self.seat_id,
                                  card_type=self.card_type,
                                  card_number=self.card_number,
                                  cvc=self.cvc, holder_name=self.holder_name)
                balance.update_balance()
                seat.change_availability()

                # Generate PDF receipt
                pdf_report = PdfReport(name=self.name, seat_id=self.seat_id, price=balance.retrieve_price())
                pdf_report.generate()

                return self.messages['purchase_successful']
            else:
                return result
        else:
            return self.messages['details_incorrect']
