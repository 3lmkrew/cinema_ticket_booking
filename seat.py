import sqlite3

# Ask for user seat number
# checks if seat is available
# if available it will update database with taken


class Seat:
    """Checks for seat number availability and removes from database if purchase"""

    def __init__(self):
        self.connection = sqlite3.connect("database/cinema.db")
        self.cursor = self.connection.cursor()
        self.availability = 2
        self.price = 0
        self.input_seat_id = input("Preferred seat number: ").title()

    def get_seat_availability(self):
        """returns 0 for available and 1 for taken"""
        self.cursor.execute(f'SELECT "taken" FROM "Seat" WHERE "seat_id" == "{self.input_seat_id}" ')
        try:
            self.availability = self.cursor.fetchone()[0]
            return self.availability
        except TypeError:
            print("Seat Availability error due to incorrect seat number!")

    def seat_id(self):
        """returns seat id number"""
        return self.input_seat_id

    def get_price(self):
        """returns seat price"""
        self.cursor.execute(f'SELECT "price" FROM "Seat" WHERE "seat_id" == "{self.input_seat_id}"')
        try:
            self.price = self.cursor.fetchone()[0]
            return self.price
        except TypeError:
            return "The seat number does not exist"

    def is_available(self):
        """returns True if seat is 0 for not-taken and updates database with 1 for taken"""
        self.get_seat_availability()
        try:
            if self.availability == 0:
                self.connection.execute(f'UPDATE "Seat" SET "taken" = 1 WHERE "seat_id" = "{self.seat_id()}" ')
                self.connection.commit()
                self.connection.close()
                return True
        except TypeError:
            print("Since seat does not exist, I cannot select")
            return False

    def is_occupy(self):
        """returns True if seat is 1 for taken"""
        if self.availability == 1:
            print(f"Seat is Taken")
            return True
