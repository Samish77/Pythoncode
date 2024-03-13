import random
# game snake water gun

def gameWin(comp,You):
    if comp==You:
        return None
    elif comp=="s":
        if You=="w":
            return False
        elif You==g:
            return True
    elif comp=="w":
        if You=="g":
            return False
        elif You=="s":
            return True
    elif comp=="g":
        if You=="s":
            return False
        elif You=="w":
            return True
        

print("computer turn:snake(s) water(w) gun(g) ?")
randno=random.randint(1,3)
if randno==1:
    comp='s'
elif randno==2:
    comp='w'
elif randno==3:
    comp='g'      

You=input("Your turn:snake(s) water(w) gun(g) ?")
a=gameWin(comp,You)

print(f"Computer choice  {comp}")
print(f"Your choice{You}")
if a==None:
    print("The game is Tie")
elif a:
    print("you won")
else:
    print("you lose")