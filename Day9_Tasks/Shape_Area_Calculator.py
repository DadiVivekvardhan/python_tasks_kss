#6. Shape Area Calculator (Polymorphism)A graphics application needs to calculate the area of different shapes. Create classes
#Circle, Rectangle, and Triangle, each having an area() method. Demonstrate polymorphism by calling the same method for different objects.

class Circle:

    def area(self):
        radius = 5
        print("Circle Area :", 3.14 * radius * radius)

class Rectangle:

    def area(self):
        length = 10
        width = 5
        print("Rectangle Area :", length * width)

class Triangle:

    def area(self):
        base = 8
        height = 6
        print("Triangle Area :", 0.5 * base * height)


c = Circle()
r = Rectangle()
t = Triangle()

c.area()
r.area()
t.area()
