# calculate factorial of number  
# 5!=5*4*3*2*1=120
# 3!-3*2*1=6

def factorial(n):
    if n==0:
        return 1
    else:
        return n*factorial(n-1)

print(factorial(3))