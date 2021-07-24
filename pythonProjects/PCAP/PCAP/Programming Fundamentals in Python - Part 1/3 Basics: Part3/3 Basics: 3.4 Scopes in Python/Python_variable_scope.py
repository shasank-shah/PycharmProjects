def function():
    global variable
    variable = 2
    print("Do i know this variable?", variable)


variable = 1
function()
print(variable)


def function(n):
    print("I got: ", n)
    n += 1
    print("I have: ", n)


variable = 1
function(variable)
print(variable)
