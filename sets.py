# sets is collection of non repetative data
s={1,2,3,4,1}
print(type(s))
print(s)

x={}
print(type(x))

b=set()
print(type(b))
b.add(4)
b.add(5)
b.add(6)
# b.add([4,5,6])
print(b)
b.add(6)
print(b)
print(len(b))
b.remove(5)
print(b)
b.add(5)
print(b)
b.pop()    # deleted any random value from set
print(b)
b.clear()
print(b)