class Account:
    interest=0.02
    def __init__(self,account_holder):
        self.balance=0
        self.holder=account_holder

    def deposit(self,amount):
        self.balance+=amount
        return self.balance
    def withdraw(self,amount):
        if  amount>self.balance:
            return "Insufficiend found"
        self.balance-=amount
        return self.balance
    
class CheckingAccount(Account):
    withdraw_charge=1
    interest=0.01
    def withdraw(self, amount):
        return Account.withdraw(self,amount+self.withdraw_charge)
    