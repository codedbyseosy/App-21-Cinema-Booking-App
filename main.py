from ClassFiles.card import Card

"""
A1-120, A2-100 A3-120, B1-100, B2-150, B3-120 
type = Visa, Master Card
number = 12345678, 23456789
cvc = 123, 234
holder = John Smith, Marry Smith (5000.0)
"""

# Gather user input for card and seat details
name = input("Enter your full name: ")
seat_id = input("Enter your preferred seat number: ")
card_type = input("Indicate your card type (Visa/Mastercard): ")
card_number = input("Enter your card number: ")
cvc = input("Enter your card cvc: ")
holder_name = input("Enter your card holder name: ")

# Create a Card object with the provided details
card = Card(name=name, seat_id=seat_id, card_type=card_type, card_number=card_number, cvc=cvc,
            holder_name=holder_name)

# Check card details and process the purchase
result = card.check_card_details()
print(result)
