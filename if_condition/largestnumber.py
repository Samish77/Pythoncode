# finding  largest number using if statement
 
num1=int(input("enter your first number"))
num2=int(input("enter the second number"))
num3=int(input("enter the third number"))
if(num1>num2):
    if(num1>num3):
        print(str(num1) + " is largest")
    else:
        print(str(num3)+ " is largest")
else:
    if(num2>num3):
       print(str(num2) + " is largest")
    else:
        print(str(num3)+ " is largest")
