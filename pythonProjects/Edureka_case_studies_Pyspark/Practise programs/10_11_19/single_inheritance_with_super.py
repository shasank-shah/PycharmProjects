class Father:
    def __init__(self):
        print("Initializing Father class")
    def swimmer(self):
        print("I am a good swimmer")

class Child(Father):
    def __init__(self):
        super(Child,self).__init__()
        print("Initializing Child class")
    def boxing(self):
        print("I am a good boxer")

c1 = Child()
print(c1.swimmer())
print(c1.boxing())