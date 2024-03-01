# Generator function example

def creater():
    i=1
    while i<201:
        yield i
        i+=1

#print(creater())
x=creater()
print(next(x))
print(next(x))
print(next(x))
print(list(x))