class Account:
    def __init__(self,acc_no,acc_pass):
        self.acc_no=acc_no
        self.__acc_pass=acc_pass

acct=Account("12345","abcde")

print(acct.acc_no)
print(acct.acc_pass)
