class person:
    __name="xyz"

    def __hello(self):
        print("hello person")
    
    def welcome(self):
        self.__hello()

p1=person()
print(p1.welcome())