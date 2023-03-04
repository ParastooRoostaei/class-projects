from abc import ABC
#----------------------------------------------parent class
class Person(ABC):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def showInfo(self):
        pass
#---------------------------------------------------child class
class Student(Person):
    def __init__(self, studentId, name, age):
        super().__init__(name, age)
        self.studentId = studentId

    def showInfo(self):
        print(f"{self.studentId}\t\t {self.name}\t\t {self.age}")
#---------------------------------------------------child class
class Teacher(Person):
    def __init__(self, teacherCode, name, age):
        super().__init__(name, age)
        self.teacherCode = teacherCode

    def showInfo(self):
        return f"teacherCode: {self.teacherCode}"
#-----------------------------------------------------objects
stu1 = Student(123,"Ali", 18)
teach1 = Teacher(451, "Ahmad", 63)
stu1.showInfo()
print(teach1.showInfo())