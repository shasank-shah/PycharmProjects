from functools import reduce

def sum(a, b):
    return a*b

list1 = [1, 2, 3, 4, 5]
print(reduce(sum, list1))

# using lambda
print("using lambda: ", reduce((lambda a,b: a*b), list1))