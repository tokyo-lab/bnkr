class Person:
    def __init__(self, firstname, lastname):
        self.firtname = firstname
        self.lastname = lastname


class Customer(Person):
    def __init__(self, account_number, balance):
        self.account_number = account_number
        self.balance = balance

    def print_info(self):
        print(f"Cutomer Name: {self.firtname} {self.lastname} \n")
        print(f"Account: {self.account_number} \n")
        print(f"Balance: {self.balance} \n")
