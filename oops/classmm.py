class person:
    name="anonymous"

    @classmethod
    def changeName(cls,name):
        cls.name=name
        

p1=person()
p1.changeName("vedant")
print(p1.name)
print(person.name)