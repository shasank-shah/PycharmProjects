class firstclass:
    pass

obj1 = firstclass()
print(obj1)

# o/p is "<__main__.firstclass object at 0x02CB8670>"

class firstclass:
    def firstmethod(selfself):
        print("My first method of class")

object1 = firstclass()
print(object1.firstmethod())

print(firstclass.__dict__)