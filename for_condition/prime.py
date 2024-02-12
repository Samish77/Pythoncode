# weather a number is prime or not
num=int(input("Enter the number to check if prime or not"))
# prime=True
for i in range(2,num-1):
    if(num%i==0):
        
        print("The number is not a prime")
        # break
    else:
        print("this is  prime number")    