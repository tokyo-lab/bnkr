class Person:
    def __init__(self, firstname, lastname):
        self.firstname = firstname
        self.lastname = lastname


class Customer(Person):
    def __init__(self, firstname, lastname, account_number, balance):
        super().__init__(firstname, lastname)
        self.account_number = account_number
        self.balance = balance

    def print_info(self):
        print(f"Cutomer Name: {self.firstname} {self.lastname} \n")
        print(f"Account: {self.account_number} \n")
        print(f"Balance: {self.balance} \n")


customer_1 = Customer("mike", "cooper", "54324324", 800.80)

customer_1.print_info()
