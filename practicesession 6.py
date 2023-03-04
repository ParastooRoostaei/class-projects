from datetime import datetime
from abc import ABC , abstractmethod
import enum
class Bookstatus(enum.Enum):
    Unselected = 1
    Selected = 2
    Translated = 3
#-----------------------------------
class Text(ABC):
    def __init__(self, lang, numberOfDay):
        self.lang = lang
        self.status = Bookstatus.Unselected
        self.numberOfDay = numberOfDay
        self.registerDate = datetime.now()

def getlang(self):
    return self.lang

def changeStatus(self, newStatus):
    self.status = newStatus

def __str__(self):
    return self.lang + "\t" + str(self.numberOfDay) + "\t" + str(self.registerDate) + "\t" + self.status

@abstractmethod
def getFee(self):
    pass
#-----------------------------------
class PlainText(Text):
    def __init__(self, lang, numberOfDay, numberWord, numberLongWord):
        super().__init__(lang, numberOfDay)
        self.__numberWord = numberWord
        self.__numberLongWord = numberLongWord

    def getFee(self):
        return self.__numberWord*500+self.__numberLongWord*600
#--------------------------------------
class ScienceText(Text):
    def __init__(self, lang, numberOfDay, numberScienceWord, numberGeneralWord):
        super().__init__(lang, numberOfDay)
        self.__numberScienceWord = numberScienceWord
        self.__numberGeneralWord = numberGeneralWord

    def getFee(self):
        return self.__numberGeneralWord*600+ self.__numberScienceWord*1000
#------------------------------------
class HumorosText(Text):
    def __init__(self, lang, numberOfDay, numberImage):
        super().__init__(lang, numberOfDay)
        self.__numberImage = numberImage

    def getFee(self):
        return self.__numberImage*300000
#---------------------------------------
class Translator:
    def __init__(self, name, family, mobile):
        self.__name = name
        self.__family = family
        self.__mobile = mobile
        self.__isActive = False
        self.__languageList = []

    def addLanguage(self, language):
        self.__languageList.append(language)

    def __str__(self):
        temp = self.__name+ "\t" +self.__family+ "\t" + self.__mobile + "\t" + str(self.__isActive) + "\n"
        for lan in self.__languageList:
            temp += lan + "\n"
        return temp 

    def selectBook(self, text):
        if self.__isActive == False:
            if text.status == Bookstatus.Unselected:
                text.changeStatus(Bookstatus.Selected)
                self.__isActive = True
            else :
                print("This text choosed befor.")
        else:
            print("you can not choose any Text.")

    def afterTranslate(self, text):
        text.changeStatus(Bookstatus.Translated)
#-------------------------------------
class Book(Text):
    def __init__(self, lang, numberOfDay):
        super().__init__(lang, numberOfDay)
        self.__textList = []

    def changeStatus(self, newStatus):
        self.status = newStatus

    def addText(self, text):
        self.__textList.append(text)

    def __str__(self):
        return self.lang + "\t" + str(self.numberOfDay)

    def getFee(self):
        sum = 0
        for text in self.__textList:
            sum += text.getFee()
        return sum
    #--------------------------------------objects
m1 = Translator("Ali", "Ahmadi", "09123758897")
m1.addLanguage("English")
m1.addLanguage("French")
print(m1)

print("-------------------")
m2 = Translator("Ahmad", "Razavi", "09153329909")
m2.addLanguage("English")
print(m2)

print("**********")
b1 = Book("English", 40)
b1.addText(PlainText("English", 12, 1200, 250))
b1.addText(ScienceText("English", 28, 3000, 1500))
print(b1)
print("~~~~~~~~~~~~~~~~~~~~")
m2.selectBook(b1)
print(b1.getFee())
print(m2)
print(b1)
m1.selectBook(b1)