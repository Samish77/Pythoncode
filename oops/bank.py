# Create a Account Class  with 2 attributes balance and Account.no. 
# Create method for debit and credit and printing the balance.

class Account:
    def __init__(self,bal,acc):
        self.balance=bal
        self.account_no=acc

    #debit method
    def debit(self,amount):
        self.balance -= amount
        print("Rs",amount,"was debited")
        print("Total Balance= ",self.get_balance())

    #credit method
    def credit(self,amount):
        self.balance += amount
        print("Rs",amount," was credited")
        print("Total Balance= ",self.get_balance())

    #printing balance
    def get_balance(self):
        return self.balance    
    

acc1=Account(10000,123)
#print(acc1.balance)
acc1.debit(1000)
acc1.credit(5000)