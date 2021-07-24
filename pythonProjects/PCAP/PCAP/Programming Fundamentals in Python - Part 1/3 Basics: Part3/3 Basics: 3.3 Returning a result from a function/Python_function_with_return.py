# return without expression
def fun(explode=True):
    print("Three...")
    print("Two...")
    print("One...")
    if not explode:
        return  # return without expression
    print("Boom!")


fun()
fun(False)


# return with expression
def boring_function():
    return 13  # return with expression


x = boring_function()
print("The boring function returned its value: ", x)


# return expression getting lost
def boring_function():
    print("What a boredom....")
    return 13  # return expression getting lost


print("Hi, boring!")
boring_function()
print("Stop whinning, please!")


# if a function doesn't return any value then it implicitly returns None
def strange(n):
    if (n % 2 == 0):
        return True


print(strange(2))
print(strange(1))

if (strange(1) == None):
    print("Even None can be manipulated")


# function with arguments as list
def sumoflist(l):
    sum = 0
    for el in l:
        sum += el
    return sum


print("arguments with list:", sumoflist([1, 2, 3]))
