#constructor 

class  student:
    name="rishi"
    def __init__(self,fullname):
       self.name=fullname
       print("Adding a new student")

s1=student("vedant")
print(s1.name)