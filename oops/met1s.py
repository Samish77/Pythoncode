# creating a class
class student:
    def __init__(self,name):
        self.name=name

    def welcome(self):
        print("welcome to the class")

    def hello(self):
        print("hello",self.name)

#creating a object
s1=student("swapnil")
s1.hello()
s1.welcome()         