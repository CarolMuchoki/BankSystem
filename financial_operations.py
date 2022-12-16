class BankAccount:
    def __init__(self):
        self.balance = 0
        print("Hello welcome to Deposit and Withdraw machine")

    def deposit(self):
        amount= float(input("Enter Amount to be deposited: "))
        self.balance += amount
        print(f"Amount Deposited:", amount)

    def withdraw(self):
        amount= float(input("Enter Amount to withdraw: "))
        if self.balance >= amount:
            self.balance -= amount
            print(f"Amount withdrawn", amount)
        else:
            print(f"Insufficient balance ")

    def display(self):
        print(f"Net Available Balance", self.balance)

operation = BankAccount()
operation.deposit()
operation.withdraw()
operation.display()


