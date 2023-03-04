from abc import ABC, abstractmethod
import enum
#----------------------------------class for delivery order
class DeliveryType(enum.Enum):
    Bike = 2500
    MotorCycle = 10000
    Drone = 80000
#---------------------------------class for size of Pizza
class Size(enum.Enum):
    Mini = 1
    Medium = 2
    Large = 5
#---------------------------------class parent for order eating items
class Item(ABC):
    def __init__(self):
        super().__init__()

    @abstractmethod
    def getCost(self):
        pass
#---------------------------------class for pizza
class Pizza(Item):
    def __init__(self, Size):
        super().__init__()
        self.basePrice = 10000
        self.Size = Size
        self.contentList = []

    def addContent(self, content):
        self.contentList.append(content)

    def getCost(self):
        sum = 0
        for content in self.contentList:
            sum+=content.getPrice()
        sum*=self.Size
        sum+=self.basePrice
        return sum
#---------------------------------class for drink
class Drink(Item):
    def __init__(self, weight, carbonated):
        super().__init__()
        self.cc = 20
        self.weight = weight
        self.carbonated = carbonated

    def getCost(self):
        if self.carbonated == True:
            return self.weight*self.cc+4000
        else :
            return self.cc*self.weight

#---------------------------------class parent for pizza contents
class Content(ABC):
    def __init__(self):
        super().__init__()

    @abstractmethod
    def getPrice(self):
        pass
#---------------------------------class tomato is content child
class Tomato(Content):
    def __init__(self, weight):
        super().__init__()
        self.unitPrice = 8000
        self.weight = weight

    def getPrice(self):
        return self.weight*self.unitPrice
#---------------------------------class mushroom is content child
class Mushroom(Content):
    def __init__(self, weight, Canned):
        super().__init__()
        self.unitPrice = 30000
        if weight>0.2:
            weight = 0.2
        self.weight = weight
        self.Canned = Canned

    def getPrice(self):
        if self.Canned ==True:
            return self.weight*self.unitPrice
        else:
            return self.unitPrice*self.weight*2
#---------------------------------class chicken is content child
class Chicken(Content):
    def __init__(self, weight):
        super().__init__()
        self.unitPrice = 45000
        self.weight = weight

    def getPrice(self):
        return self.weight*self.unitPrice
#---------------------------------class chickenHam is content child
class ChickenHam(Content):
    def __init__(self,weight):
        super().__init__()
        self.unitPrice = 120000
        self.weight = weight

    def getPrice(self):
        return self.weight*self.unitPrice
#---------------------------------class redMeat is content child
class RedMeat(Content):
    def __init__(self, weight):
        super().__init__()
        self.unitPrice = 200000
        if weight>0.15:
            weight =0.15
        self.weight = weight

    def getPrice(self):
        return self.unitPrice*self.weight
#---------------------------------class cheese is content child
class Cheese(Content):
    def __init__(self, weight):
        super().__init__()
        self.unitPrice = 180000
        self.weight = weight

    def getPrice(self):
        return self.weight*self.unitPrice
#---------------------------------class for orders
class Order:
    def __init__(self, deliveryType):
        self.DeliveryType = deliveryType
        self.OrderItems = []

    def addItem(self, item):
        self.OrderItems.append(item)

    def getTotalcost(self):
        sum = self.DeliveryType
        for item in self.OrderItems:
            sum += item.getCost()
        return sum
#----------------------------------------objects
p1 = Pizza(Size.Medium.value)
p1.addContent(Tomato(0.2))
p1.addContent(Mushroom(0.3, True))
p1.addContent(Cheese(0.4))
p1.addContent(Chicken(0.3))

p2 = Pizza(Size.Mini.value)
p2.addContent(Cheese(0.2))
p2.addContent(RedMeat(0.1))

d1 = Drink(300, False)
d2 = Drink(400, True)

orderMehdi = Order(DeliveryType.MotorCycle.value)
orderMehdi.addItem(p1)
orderMehdi.addItem(d1)
orderMehdi.addItem(p2)
orderMehdi.addItem(d2)

print(orderMehdi.getTotalcost())