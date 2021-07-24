def fact(_fact):
    _factResult = 1
    if _fact in (0, 1):
        print("The factorial of ", _fact, " is: 1")
    elif _fact < 0:
        print("The factorial of ", _fact, " cannot be determined due to negative values")
    elif _fact > 1:
        for i in range(_fact, 1, -1):
            _factResult = _factResult * i
        print("The factorial of given number", _fact, " is: ", _factResult)
    else:
        print("There is some issue with fact number")
_fact = int(input("Enter number: "))
fact(_fact)