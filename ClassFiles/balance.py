import sqlite3


class Balance:
    """
    Retrieves the price of a seat in a cinema as well as
    updates the balance in a user's card after purchasing a seat
    and extracts the new balance.
    """

    def __init__(self, seat_id, card_type, card_number, cvc, holder_name):
        self.seat_id = seat_id
        self.card_type = card_type
        self.card_number = card_number
        self.cvc = cvc
        self.holder_name = holder_name

    def retrieve_price(self):
        # Connect to the cinema database to retrieve the seat price
        connection = sqlite3.connect("databases/cinema.db")
        cursor = connection.cursor()
        cursor.execute("""SELECT price FROM Seat WHERE seat_id = ?""", [self.seat_id])
        result = cursor.fetchone()
        connection.close()

        if result:
            return result[0]  # Ensure this is a single numeric value
        else:
            return 0  # Handle case where price is not found

    def update_balance(self):
        # Retrieve the price of the seat
        price = self.retrieve_price()
        print(f"Price retrieved for seat {self.seat_id}: {price}")

        # Update the balance in the banking database
        connection = sqlite3.connect("databases/banking.db")
        cursor = connection.cursor()
        cursor.execute("""
            UPDATE Card SET balance = balance - ?
            WHERE type = ? AND number = ? AND cvc = ? AND holder = ?""",
                       (price, self.card_type, self.card_number, self.cvc, self.holder_name))
        connection.commit()

        # Extract and print the updated balance
        updated_balance = self.extract_updated_balance(connection, cursor)
        print(f"Updated balance for card {self.card_number}: {updated_balance}")

        return updated_balance

    def extract_updated_balance(self, connection, cursor):
        # Fetch the updated balance from the database
        cursor.execute("""
            SELECT balance FROM Card
            WHERE type = ? AND number = ? AND cvc = ? AND holder = ?""",
                       (self.card_type, self.card_number, self.cvc, self.holder_name))
        result = cursor.fetchone()
        connection.close()

        if result:
            return result[0]  # Return the updated balance
        else:
            return 0  # Handle case where balance is not found (though unlikely if the card details are correct)
