# def func1():
#         return "parastoo"
# def func2():
#         yield "parastoo"
#         yield "ali"
#         yield "hello"

# print(func1())
# #print(func2())

# for item in func2():
#         print("******************")
#         print(item)

# l = list(func2())
# print(l)
# s = set(func2())
# print(s)
# obj1 = func2()
# print(next(obj1))
# print(next(obj1))
#------------------------------------------------
def fib(n):
        a = 0
        b = 1
        yield b
        for i in range(1,n):
                a,b = b,a+b
                yield b
        
for i in fib(5):
        print(i, end="\t")
        