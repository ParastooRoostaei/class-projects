class Person:
    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    def showPersonInfo(self):
        print(self.__name)
        print(self.__age)

    def __eq__(self,obj2):
        return self.__name == obj2.__name  and  self.__age == obj2.__age

    def __hash__(self) -> int:
         return hash(self.__name)+hash(self.__age)

    def __str__(self) -> str:
         return f"Name: {self.__name}\t   Age: {self.__age}"

person1 = Person("ali",23)
person2 = Person("mehdi",41)
person3 = Person("ali",23)

set = {person1, person2, person3}
for person in set:
    print(person)
    