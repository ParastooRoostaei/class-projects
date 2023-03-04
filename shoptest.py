class Product:
    def __init__(self, productId, productName, price):
        self.productId = productId
        self.productName = productName
        self.price = price

    def showProductInfo(self):
        print(f'Code : {self.productId}\tName : {self.productName}\tPrice : {self.price}\t')



class Cloth(Product):
    def __init__(self, productId, productName, price, size, color):
        super().__init__(productId, productName, price)
        self.size = size
        self.color = color
    
    def __str__(self):
        return f'Code : {self.productId}\tName : {self.productName}\tPrice : {self.price}\tSize : {self.size}\tColor : {self.color}\t'


class Food(Product):
    def __init__(self, productId, productName, price,expirationDate):
        super().__init__(productId, productName, price)
        self.expirationDate = expirationDate

    def __str__(self):
        return f'Code : {self.productId}\tName : {self.productName}\tPrice : {self.price}\tExpirationDate : {self.expirationDate}\t'



class Appliances(Product):
    def __init__(self, productId, productName, price, brand, model, color):
        super().__init__(productId, productName, price)
        self.brand = brand
        self.model = model
        self.color = color

    def __str__(self):
        return f'Code : {self.productId}\tName : {self.productName}\tPrice : {self.price}\tBrand : {self.brand}\tModel : {self.model}\tColor : {self.color}'


code=int(input("Enter Prouduct Code : "))
name=input("Enter Prouduct Name : ")
price=int(input("Enter Prouduct Price : "))
brand=input("Enter Prouduct Brand : ")
model=input("Enter Prouduct Model : ")
color=input("Enter Prouduct Color : ")
product5=Appliances(code,name,price,brand,model,color)
print(product5)


