# The *c will store n arguments in tuple.
def sum(a, b, *c):
    _sum = 0
    _sum += a + b
    for index in c:
        _sum += index
    print(_sum)

sum(10, 20, 30, 40, 50, 60)

# The **c will store n arguments in dictionary.
def mul(a, b, **c):
    _mul = 1
    _mul = a * b
    print(_mul)
    for value in c.values():
        _mul = _mul * value
    print(value)

mul(1, 2, c=1, d=2, e=1, f=2, g=3)
