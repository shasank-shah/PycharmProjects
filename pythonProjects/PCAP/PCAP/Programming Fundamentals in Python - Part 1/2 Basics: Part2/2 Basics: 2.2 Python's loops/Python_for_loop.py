for i in range(10):
    print("i: ", i)

for i in range(2, 8):
    print("new i: ", i)

for i in range(1, 1):
    print("The body will not execute")

for i in range():
    print("The body will not execute")

for i in range(2, 1):
    print("The body will not execute as the first value is greater than second")
