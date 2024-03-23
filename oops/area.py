# radius of circle is given.. calculate area and perimeter of circle.
# we need use class and object method.

class circle:
    def __init__(self,radius):
        self.radius=radius

    def area(self):
        return (22/7) * self.radius **2
    
    def perimeter(self):
        return 2 *(22/7) *self.radius

c1=circle(7)
print(c1.area())
print(c1.perimeter())

