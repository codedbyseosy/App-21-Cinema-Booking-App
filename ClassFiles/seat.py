import sqlite3


class Seat:
    """
    Checks whether or not a seat is available and if it is changes
    the availability of the seat if it is purchased.
    """
    messages = {
        "purchase_successful": "Purchase was successful! Enjoy your movie.",
        "seat_unavailable": "The seat selected is unavailable. Please select another.",
        "seat_exist": "No such seat exists."
    }

    def __init__(self, seat_id):
        self.seat_id = seat_id

    def seat_availability(self):
        # Connect to the cinema database to check seat availability
        connection = sqlite3.connect("databases/cinema.db")
        cursor = connection.cursor()
        cursor.execute("""SELECT taken FROM Seat WHERE seat_id = ?""", (self.seat_id,))
        result = cursor.fetchone()

        if result is None:
            return self.messages['seat_exist']
        else:
            if result[0] == 0:
                self.change_availability()
                return self.messages['purchase_successful']
            else:
                return self.messages['seat_unavailable']

    def change_availability(self):
        # Update the seat availability in the database
        connection = sqlite3.connect("databases/cinema.db")
        connection.execute("""
            UPDATE Seat SET taken = 1 WHERE seat_id = ?
            """, (self.seat_id,))
        connection.commit()
        connection.close()
