# def mainFun(func):
#         def func1():
#                 print("+++++++++++++++++++")
#                 func()
#                 print("*******************")
#         return func1

# def printName():
#         print("parastoo")

# f = mainFun(printName)
# f()
#-----------------------------------------------
def mainFunc(func):
        def func1():
                print("#########################")
                for i in range(6):
                        func()
                print("#########################")
        return func1

@mainFunc
def printName():
        print("Parastoo ")

printName()

