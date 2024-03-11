class car:
    color="black"

    @staticmethod
    def start():
        print("car started...")

    @staticmethod
    def stop():
        print("car stopped")

class toyatocar(car):
      def __init__(self,brand):
         self.brand=brand
         print(brand)

class fortuner(toyatocar):

    def __init__(self,type):
        self.type=type
        print(type)


car1=fortuner("disel")

print(car1.start())
print(car1.color)