class car:
    def __init__(self,type):
        self.type=type
    
    @staticmethod
    def start():
        print('car started....')

class  Toyotocar(car):
    def __init__(self,name,type):
        super().__init__(type)
        super().start()
        self.name=name
        self.type=type
        

car1=Toyotocar("innova","electric")
print(car1.name)
print(car1.type)