# -*- coding: utf-8 -*-
# -*- created by Alex Marchenko -*-


class BankAccount():

    def __init__(self, client = "Name Surname", currency = "€", balance = 0.0):

        self.client = client
        self.currency = currency
        self.balance = balance


    def checkacc (self):

        print("\nAccount Name: {};\nAccount balance: {}{:0.2f};\n".format(self.client, self.currency, self.balance))


    def deposit (self):

        amount = float(input(f"{self.client}, how much would you like to deposit? "))
        self.balance = self.balance + amount
        print (f"The amount {self.currency}{amount} has been added to your account.\n")


    def withdraw (self):

        amount = float(input(f"{self.client}, how much would you like to withdraw? "))
        if self.balance < amount:
            print(f"Sorry, you do not have enough funds on the account for this transaction.\n")
        else:
            self.balance = self.balance - amount
            print(f"The amount {self.currency}{amount} has been withdrawn from your account.\n")
            print(f"The available balance on your account is {self.currency}{self.balance}")


    def __str__ (self):
        return "\nAccount Name: {};\nAccount balance: {}{:0.2f};\n".format(self.client, self.currency, self.balance)



a = BankAccount("Alex Marchenko")
print (a)
a.deposit()
a.withdraw()
print(a)
a.withdraw()
print(a)
a.checkacc()