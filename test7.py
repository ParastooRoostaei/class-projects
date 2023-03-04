class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def showPersonInfo(self):
        print(self.name)
        print(self.age)

    @staticmethod
    def sum(x,y):
        return x+y
    
    @classmethod
    def fun1(cls, x, y):
        return cls.sum(x,y)+2000


person1 = Person("mehdi", 41)
person1.showPersonInfo()

print(Person.sum(20,40))

print(Person.fun1(3,25))