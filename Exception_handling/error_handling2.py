try:
    num=int(input("enter an integer"))
    a=[5,4]
    print(a[num])
    
except ValueError:
    print("Number entered is not an intger")

except IndexError:
    print("Index Error")