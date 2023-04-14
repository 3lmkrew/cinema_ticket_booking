import pdf_ticket
from credit_card import Card
from seat import Seat
from pdf_ticket import Ticket

""""
----------------------------------------------------------------------------------------------------------
-    Title:       Cinema Ticket Booking App                                                              -
-    Description: An app where a user can book a cinema seat using SQL databases                         -
-    Course:      Chapter 10 in OOP (Advance Python Object Oriented Programming)                         -
-    Author:      Mason Hernandez                                                                        -
-    Date:        February, 26 2023                                                                      -
----------------------------------------------------------------------------------------------------------
----------------------------------------------------------------------------------------------------------
-                              --Basic Functionality--                                                   -
-    Seat is NOT available - *ERROR*                                                                     -
-    Seat is available BUT Credit Card is invalid OR has insufficient funds  *ERROR*                     -
-    Seat is available and Credit Card has sufficient amount to purchase ticket **PASS**                 -
-    If **PASS** Updates Seat & Card Databases and returns digital ticket PDF                            -
----------------------------------------------------------------------------------------------------------
"""


class User:
    """Asks for users name"""
    def __init__(self, user_name):
        self.user_name = user_name

    @staticmethod
    def buy(seat, card):
        """ requires seat object and card object to check if seat is available and funds are sufficient"""
        if card.validate(ticket_price) and seat.is_available():
            return True
        else:
            seat.is_occupy()


if __name__ == "__main__":
    user = User(input("Type Your full name: ").title())  # user object
    my_seat = Seat()  # seat object
    my_card = Card()  # card object
    ticket_price = my_seat.get_price()  # ticket cost
    seat_selection = my_seat.seat_id()  # seat number
    random_id = pdf_ticket.ticket_id()  # random ticket id
    buy = user.buy(my_seat, my_card)  # returns True if seat available and card approved.
    if buy:
        ticket = Ticket(id_seat=random_id, user_name=user.user_name, price=ticket_price,  # creates PDF movie ticket
                        seat=seat_selection)
        ticket.to_pdf(f"ticket_folder/{user.user_name}_ticket.pdf")
        print("Purchase successful")
