#Q.Online Shopping System (Multilevel Inheritance)
#An e-commerce company organizes products using multiple levels. Create classes Product → ElectronicProduct → MobilePhone using multilevel inheritance and
#display product details.

class Product:

    def __init__(self, name):
        self.name = name

class ElectronicProduct(Product):

    def __init__(self, name, brand):
        Product.__init__(self, name)
        self.brand = brand

class MobilePhone(ElectronicProduct):

    def __init__(self, name, brand, price):
        ElectronicProduct.__init__(self, name, brand)
        self.price = price

    def display(self):
        print("Product Name :", self.name)
        print("Brand :", self.brand)
        print("Price :", self.price)


m = MobilePhone("Smartphone", "Samsung", 25000)

m.display()
