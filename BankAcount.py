class BankAccount:

    def __init__(self):
        self.__balance = 0
    
    def credit(self, amount):
        self.__balance += amount
    
    def debit(self, amount):
        self.__balance -= amount
    
    def get_balance(self):
        return self.__balance

Amy = BankAccount()

Amy.credit(100)
Amy.debit(30)
print(Amy.get_balance())
Amy.__balance = 1000
print(Amy.get_balance())

print(BankAccount.__balance)
