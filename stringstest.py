# Program to reverse a string
a="Hello world"
print(a[::-2])

#   : starting index
#   : ending index
#   -1   all letters are printed      -2 one gap letter.
# join and reverse method
a="".join(reversed(a))
print(a) 

# Deleting/Updating string      string is consider to be immutable data type
#  string into list
string1="Welcome to india"
print(string1)
list1=list(string1)
list1[2]='p'
print(list1)
string2="".join(list1)
print(string2)

string3=string1[0:2] + string1[3:]
print(string3)


replace(" ","")