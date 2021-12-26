# bank_account

class bank_account:
    def __init__(self, name):
        self.owner = name
        self.ballance = 0.0

    def getBalance(self):
        return self.ballance

    def deposit(self, amount):
        self.ballance += amount
        return self.ballance

    def withdraw(self, amount):
        self.ballance -= amount
        return self.ballance




account1 = bank_account("Colt") 
account2 = bank_account("John")

print(account1.owner)
print(account2.owner)
print(account1.ballance)
print(account2.ballance)
print(account1.deposit(100))
print(account1.ballance)
print(account2.deposit(200))
print(account1.withdraw(30))
print(account1.ballance)


