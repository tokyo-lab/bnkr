import os


def clear_screen():
    # Clear the screen, platform independent
    os.system("cls" if os.name == "nt" else "clear")


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
        print(f"Balance: ${self.balance:.2f} \n")

    def deposit(self):
        try:
            deposit_amount = float(input("Enter an amount to deposit: "))
            self.balance += deposit_amount
            print(f"The new balance is ${self.balance:.2f}")
        except ValueError:
            print("Invalid input. Please enter a numeric value")

    def withdraw(self):
        try:
            withdraw_amount = float(input("Enter an amount to withdraw: "))
            if withdraw_amount <= self.balance:
                self.balance -= withdraw_amount
                print(f"The new balance is ${self.balance:.2f}")
            else:
                print(f"Insufficient funds. Your balance is ${self.balance:.2f}.")
        except ValueError:
            print("Invalid input. Please enter a numeric value")


def start():
    # clear_screen()
    print("*" * 50)
    print("*" * 5 + " Welcome to bnkr " + "*" * 5)
    print("*" * 50)
    print("\n")

    menu_choice = "x"
    while not menu_choice.isnumeric() or int(menu_choice) not in range(1, 5):
        print("Choose an option: ")
        print(
            """
[1] - View My Info
[2] - Deposit Money
[3] - Withdraw Money
[4] - End Program
              """
        )
        menu_choice = input()

    return int(menu_choice)


def return_begining():
    return_choice = "x"

    while return_choice.lower() != "b":
        return_choice = input("\nPress 'b' to return home")


# menu = start()
# print(menu)

finish_program = False
customer_1 = Customer("mike", "cooper", "54324324", 800)
while not finish_program:
    menu = start()
    if menu == 1:
        print("menu item 1 selected")
        customer_1.print_info()
    elif menu == 2:
        print("menu item 2 selected")
        customer_1.deposit()
    elif menu == 3:
        print("menu item 3 selected")
        customer_1.withdraw()
    elif menu == 4:
        print("menu item 4 selected")
        finish_program = True
        return_begining()
