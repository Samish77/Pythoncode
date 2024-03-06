# program to calculate Average of marks of 3 subjects sing constructor
class student:
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks
    # static function 
    @staticmethod
    def hello():
        print("hello")

    def get_avg(self):
        sum=0
        for val in self.marks:
            sum += val
        print("hello",self.name,"your average is=",sum/3)

s1=student("vedant",[90,87,20])
s1.get_avg()
s2=student("swapnil",[78,79,90])
s2.get_avg()
student.hello()