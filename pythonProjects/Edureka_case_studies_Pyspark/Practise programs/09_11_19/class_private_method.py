class firstclass:
    def publicMethod(self):
        print("This is public method!")
    def __privateMethod(self):
        print("This is private method and it is still accessible!")

obj = firstclass()
print(obj.publicMethod())
print(obj._firstclass__privateMethod())