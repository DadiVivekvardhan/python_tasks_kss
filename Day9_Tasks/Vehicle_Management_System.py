#5. Vehicle Management System (Inheritance) A transport company manages different vehicles. Create a base class Vehicle with
#attributes like brand and speed. Create derived classes Car and Bike that inherit from Vehicle and display their details.

class Vehicle:

    def __init__(self, brand, speed):
        self.brand = brand
        self.speed = speed


class Car(Vehicle):

    def display(self):
        print("Car Brand :", self.brand)
        print("Car Speed :", self.speed)
class Bike(Vehicle):

    def display(self):
        print("Bike Brand :", self.brand)
        print("Bike Speed :", self.speed)


c = Car("Toyota", 180)
b = Bike("Yamaha", 120)

c.display()
print()
b.display()
