class Father:
    def swimmer(self):
        print("I am a good swimmer and can swim 2km/hr")
class Child(Father):
    def boxing(self):
        print("I am a good boxer and can knock down 2 at a time")
    def swimmer(self):
        print("I am a good swimmer as well and can swim 3km/hr")

f1 = Father()
c1 = Child()
print(f1.swimmer())
print(c1.swimmer())