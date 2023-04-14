import sqlite3


# Ask for users credit card data
# checks if card data is valid
# if valid, checks balance if higher than seat price
# subtracts seat price and updates database

class Card:

    def __init__(self):
        self.connection = sqlite3.connect("database/banking.db")
        self.curser = self.connection.cursor()
        self.card_type_input = input("Your credit card type: ").title()
        self.card_number_input = input('Your credit card number: ')
        self.card_cvc_input = input('Your credit card cvc: ')
        self.card_name_input = input('Credit card holder name: ').title()
        self.balance_amount = 0
        self.my_dic = {}

    def card_type(self):
        """returns card type if card number input matches"""
        self.curser.execute(f'SELECT "type" FROM "Card" WHERE "type" == "{self.card_type_input}"')
        try:
            self.card_type_input = self.curser.fetchone()[0]
            return self.card_type_input
        except TypeError:
            self.my_dic["Incorrect card type"] = self.card_type_input

    def card_number(self):
        """returns card number if card number input matches"""
        self.curser.execute(f'SELECT "number" FROM "Card" WHERE "number" == "{self.card_number_input}" ')
        try:
            self.card_number_input = self.curser.fetchone()[0]
            return self.card_number_input
        except TypeError:
            self.my_dic["Incorrect card numbers"] = self.card_number_input

    def card_cvc(self):
        """returns card cvc if card number input matches"""
        self.curser.execute(f'SELECT "cvc" FROM "Card" WHERE "cvc" == "{self.card_cvc_input}"')
        try:
            self.card_cvc_input = self.curser.fetchone()[0]
            return self.card_cvc_input
        except TypeError:
            self.my_dic["Incorrect card cvs"] = self.card_cvc_input

    def card_name(self):
        """returns card name if card number input matches"""
        self.curser.execute(f'SELECT "holder" FROM "Card" WHERE "holder" == "{self.card_name_input}"')
        try:
            self.card_name_input = self.curser.fetchone()[0]
            return self.card_name_input
        except TypeError:
            self.my_dic["Incorrect card name"] = self.card_name_input

    def balance(self):
        """returns account balance if card number input matches"""
        self.curser.execute(f'SELECT "balance" FROM "Card" WHERE "number" == "{self.card_number_input}"')
        try:
            self.balance_amount = self.curser.fetchone()[0]
            return self.balance_amount
        except TypeError:
            return False

    def validate(self, price):
        """requires seat price as argument, returns True if balance is sufficient,
        subtracts value of seat and updates database"""
        the_type = self.card_type()
        the_numbers = self.card_number()
        the_cvc = self.card_cvc()
        the_name = self.card_name()
        self.balance()
        pass_list = []

        if the_type == self.card_type_input:
            pass_list.append(the_type)

        if the_numbers == self.card_number_input:
            pass_list.append(the_numbers)

        if the_cvc == self.card_cvc_input:
            pass_list.append(the_cvc)

        if the_name == self.card_name_input:
            pass_list.append(the_name)

        try:
            if len(pass_list) == 4 and self.balance_amount > price:
                new_balance = self.balance_amount - price
                self.connection.execute(f"""
                                        UPDATE "Card" SET "balance" = "{new_balance}" WHERE "number" == "{the_numbers}" 
                                        """)
                self.connection.commit()
                self.connection.close()
                if len(self.my_dic) > 1:
                    print(self.my_dic)
                return True
            else:
                print(f"\nThere was a problem with your card, please check: {self.my_dic}")

        except TypeError:
            print("Seat number does not exist! Cannot retrieve seat Data. Try again.")
