class Father:
    def __init__(self):
        super(Father, self).__init__()
        print("Initializing Father class")
    def swimmer(self):
        print("I am a good swimmer")

class Mother:
    def __init__(self):
        super(Mother, self).__init__()
        print("Initializing Mother class")
    def chef(self):
        print("I am a good chef!")

class Child(Father, Mother):
    def __init__(self):
        super(Child, self).__init__()
        print("Initializing Child class")
    def boxing(self):
        print("I am a good boxer")

c1 = Child()
print(c1.swimmer())
print(c1.chef())
print(c1.boxing())