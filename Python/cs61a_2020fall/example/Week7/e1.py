def make_withdraw(balance):
    """Return a withdraw function with a starting balance."""
    def withdraw(amount):
        nonlocal balance
        if amount>balance:
            return 'Insufficient funds'
        balance-=amount
    return withdraw

def make_withdraw_list(balance):
    b=[balance]
    def withdraw(amount):
        if amount>b[0]:
            return "Insufficient funds"
        b[0]=b[0]-amount
        return b[0]
    return withdraw

t=[1,2,3]
t[1:3]=[t]
print(t)