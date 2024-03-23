a= input("enter the number")
print(f"Multipication table of {a} is :")
  

try:
   for i in range(1,11):
     print(f"{int(a)} x {i}={int(a)*i}")
except:
   print("Sorry you have entered string data")

print("Some important line of codes ")
print("end of program")