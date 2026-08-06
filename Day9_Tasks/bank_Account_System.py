#4. Bank Account System (Class, Object, Constructor) A bank wants to manage customer accounts. Create a BankAccount class with a
#constructor to initialize account number and balance. Implement methods to deposit,withdraw, and display balance.


class BankAccount:

    def __init__(self, account_number, balance):
        self.account_number = account_number
        self.balance = balance
        
    def deposit(self, amount):
        self.balance = self.balance + amount

        
    def withdraw(self, amount):
        self.balance = self.balance - amount

    def display(self):
        print("Account Number :", self.account_number)
        print("Balance :", self.balance)


b = BankAccount(12345, 10000)

b.deposit(5000)
b.withdraw(2000)

b.display()
