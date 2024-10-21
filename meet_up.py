class Account:
    def __init__(self, account_number, balance=0):
        self.account_number = account_number
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
        else:
            print("Insufficient balance")

class SavingAccount(Account):
    def __init__(self, account_number, balance, interest_rate):
        super().__init__(account_number,)

        # Parent class
class Account:
    def __init__(self, account_number, balance):
        self.account_number = account_number  # Attribute
        self.balance = balance  # Attribute

# Child class inheriting from Account
class SavingAccount(Account):
    def __init__(self, account_number, balance, interest_rate):
        # Call the parent class's __init__ method
        super().__init__(account_number, balance)
        # Additional attribute for SavingAccount
        self.interest_rate = interest_rate 
