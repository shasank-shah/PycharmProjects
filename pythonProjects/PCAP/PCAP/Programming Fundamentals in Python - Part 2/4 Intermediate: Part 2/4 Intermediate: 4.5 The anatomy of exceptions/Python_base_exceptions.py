try:
    y = 1/0
except ArithmeticError:
    print("Problem?")
print("The END")

try:
    y = 1/0
except ZeroDivisionError:
    print("Zero division error")
except ArithmeticError:
    print("Arithmetic error")

def badfun(n):
    try:
        return 1/n
    except ArithmeticError:
        print("Sorry arithmetic error!!!")
    return None

badfun(0)
print("The END of func")

def badfun1(n):
    return 1/n

try:
    badfun1(0)
except ArithmeticError:
    print("Arithmetic error in badfun1 func")
print("The END")

def badfun2(n):
    raise ZeroDivisionError

try:
    badfun2(0)
except ArithmeticError:
    print("What did you do?")
print("One more END")

def badfun3(n):
    try:
        return 1/0
    except:
        print("I did it again!!!!")
        raise

try:
    badfun3(0)
except ArithmeticError:
    print("I see!!!!")

print("All right, it THE END")

import math
x = float(input("Enter x:"))
assert x > 0.0
x = math.sqrt(x)
print(x)


