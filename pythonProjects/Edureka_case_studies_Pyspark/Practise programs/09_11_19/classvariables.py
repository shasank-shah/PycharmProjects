class firstclass:
    def firstmethod(self):
        self.pubvar = 10
        self._protected = 'This is protected variable and its a notion to be used by a programmer in sub class, but for outside world it is still a public variable.'
        self.__private = 'This is a private variable and it still can be accessible using class name.'

obj = firstclass()
obj.firstmethod()
print(obj.pubvar)
print(obj._protected)
# print(obj.__private) # If we access directly through an object, we will get an error
print(obj._firstclass__private)

obj.pubvar = 30
obj._protected = 'Again changed projected variable'
obj._firstclass__private = 'Again changed private variable'
print(obj.pubvar)
print(obj._protected)
print(obj._firstclass__private)