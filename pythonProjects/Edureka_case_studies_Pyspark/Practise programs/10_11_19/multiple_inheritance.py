class Father:
    def swimmer(self):
        print("I am a good swimmer")

class Mother:
    def chef(self):
        print("I am a good chef!")

class Child(Father, Mother):
    def boxing(self):
        print("I am a good boxer")

c1 = Child()
print(c1.swimmer())
print(c1.chef())
print(c1.boxing())