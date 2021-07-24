# two types - instance variables & Class(static) variable

class Car:
    wheels = 4              # class variable stored in class namespace
    def __init__(self):     # instance variables stored in object/instance namespace
        self.mil = 10
        self.com = "BMW"

c1 = Car()
c2 = Car()

c1.mil = 8

print(c1.com, c1.mil, c1.wheels)
print(c2.com, c2.mil, c2.wheels)