# generator function working

# create program display 1 to 200 numbers using a list
import sys
def creater():
    list=[]
    i=1
    while i<201:
        list.append(i)
        i+=1
    return list

print(creater())  
z=sys.getsizeof(list) 
print(z) 
