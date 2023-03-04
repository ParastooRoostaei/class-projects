#def func1(name):
#       return "Hello "+name

#print(func1("parastoo"))

#func2 = func1
#print(func1("ali"))
#del func1
#print(func1("sara"))
#print(func2("sara"))


#def func1(name):
#        print("insidee in func1 "+ name)
#        def func2():
#                return "inside in func2"

#        def func3():
#                return "inside in func3"
#        print("inside in func1 "+ name)
#        print(func2())

#func1("parastoo")
#print(func2())

#---------------------------------------------------------------

# def func1(text):
#         return "*"+text+"+"

# def func2(text):
#         str1 = ""
#         for i in range(5):
#                 str1+= text
#         return str1

# def mainFunc(func):
#         print(func("Parastoo"))
#         print("----------------------")

# def mainFunc2(funcA, funcB, name):
#         print(funcA(name))
#         print(funcB(name))
#         print("ääääääääääääääääääääääääääää")

# mainFunc(func1)
# mainFunc(func2)
# mainFunc2(func1, func2, "PARASTOO")
#------------------------------------------------------------------------------
# def mainFunc(name):
#         def func1():
#                 print(name)
#         print("---------------------")
#         return func1

# f1 = mainFunc("parastoo")
# print(f1())
# print("öööööööööööööö")
# f1()
#------------------------------------------------------------------------------
def calcFunc(n):
        def sum(x,y):
                return x+y

        def sub(x,y):
                return x-y

        def mul(x,y):
                return x*y
                
        def div(x,y):
                return x/y

        if n == 1 :
                return sum      
        elif n == 2 :
                return sub
        elif n == 3 :
                return mul
        elif n == 4 :
                return div

counter = int(input("enter one nuber in range 0 , 4: "))
m = calcFunc(counter)
firstNumber = int(input())
secondNumber = int(input())
print(m(firstNumber, secondNumber))