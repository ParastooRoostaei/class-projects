class Person:
    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    def showPersonInfo(self):
        print(self.__name)
        print(self.__age)

    @property
    def name(self):
        return self.__name
    
    @name.setter
    def name(self, name):
        self.__name = name


person1 = Person("mehdi", 41)
person1.showPersonInfo()

print(person1.name)
person1.name = "ahmad"
person1.showPersonInfo()


