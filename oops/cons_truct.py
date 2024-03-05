#constructor 

class  student:
    college_name="SBGI"
    def __init__(self):
        print("default constructor")

    def __init__(self,name,marks):  # Parameterised constructor
       self.name=name
       self.marks=marks
       print("Adding a new student")

s1=student("vedant",97)
print(s1.name,s1.marks)
print(student.college_name)

s2=student ("rishi",90)
print(s2.name,s2.marks)
print(s2)
print(student.college_name)