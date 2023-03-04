import enum

class DeliveryType(enum.Enum):
    Bike = 2500
    MotorCycle = 10000
    Drone = 80000

print(DeliveryType.Bike.value)


