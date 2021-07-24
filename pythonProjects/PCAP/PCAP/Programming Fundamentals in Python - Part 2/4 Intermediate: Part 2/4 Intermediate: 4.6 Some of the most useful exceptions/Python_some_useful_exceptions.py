x = input("Enter string:")
assert x != "\tS"
print(x)

list = [1, 2, 3, 4, 5]
ix = 0
doit = True

while doit:
    try:
        print(list[ix])
        ix += 1
    except IndexError:
        doit = False

print("Done")

from time import sleep

'''
seconds = 0
while True:
    try:
        print(seconds)
        seconds += 1
        sleep(1)
    except KeyboardInterrupt:
        print("Don't do that!!!")

string = 'x'
try:
    while True:
        string = string + string
        print(len(string))
except MemoryError:
    print("This is not funny")
'''

dict = {'a':'b', 'b':'c', 'c':'d'}
ch = 'a'
try:
    while True:
        ch = dict[ch]
        print(ch)
except KeyError:
    print('No such key:', ch)