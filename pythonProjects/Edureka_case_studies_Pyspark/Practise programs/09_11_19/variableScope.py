#global _vara
_vara = 20
def func():
    global _vara
    _vara = 40
    return _vara

print(_vara)
print(func())
print(_vara)