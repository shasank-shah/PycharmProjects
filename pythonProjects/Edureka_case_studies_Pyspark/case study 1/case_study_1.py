import sys
from time import gmtime, strftime
import math

# 1. A Robot moves in a Plane starting from the origin point (0,0). The robot can move toward UP, DOWN, LEFT, RIGHT. The trace of Robot movement is as given following:


# 2. Data of XYZ company is stored in sorted list. Write a program for searching specific data from that list.
# Hint: Use if/elif to deal with conditions.
list1 = [10, 20, 30, 40, 50]
search = int(input("Enter search: "))
if search in list1:
    print("The search result: ", search, " is present in list")
elif search not in list1:
    print("The search result: ", search, " is not present in list")
else:
    print("There is an issue in search result: ", search)

# 3. Weather forecasting organization wants to show is it day or night. So, write a
# program for such organization to find whether is it dark outside or not.
# Hint: Use time module.
day_night = int(strftime("%H"))
if day_night >= 18:
    print("It's night now")
else:
    print("It's day now")


# 4. Write a program to find distance between two locations when their latitude and longitudes are given.
# Hint: Use math module.
def calculateDistance(x1, y1, x2, y2):
    dist = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
    return dist


x1 = int(input("Enter x latitude: "))
x2 = int(input("Enter x longitude: "))
y1 = int(input("Enter y latitude: "))
y2 = int(input("Enter y longitude: "))
print(calculateDistance(x1, y1, x2, y2))


# 5. Design a software for bank system. There should be options like cash withdraw,
# cash credit and change password. According to user input, the software should
# provide required output.
# Hint: Use if else statements and functions.

def bankSystem(options):
    if options == 1:
        print("You have selected cash withdraw option")
    elif options == 2:
        print("You have selected cash credit option")
    elif options == 3:
        print("You have selected change password option")
    else:
        print("There are no such option available")


print("Enter 1 for cash withdraw")
print("Enter 2 for cash credit")
print("Enter 3 for change password")
option = int(input("Enter above options: "))
bankSystem(option)

# 6. Write a program which will find all such numbers which are divisible by 7 but are
# not a multiple of 5, between 2000 and 3200 (both included). The numbers obtained
# should be printed in a comma separated sequence on a single line.
for number in range(2000, 3201):
    if (number % 7 == 0) and (number % 5 != 0):
        print(number, end=", ")


# 7. Write a program which can compute the factorial of a given numbers. Use recursion to find it.
# Hint: Suppose the following input is supplied to the program: 8
# Then, the output should be: 40320
def factorial(n):
    value = 1
    if n < 0:
        print("Couldn't get factorial for negative integers: ", n)
        sys.exit(0)
    elif n == 0 or n == 1:
        print("The factorial of a given number: ", n, " is: ", value)
        sys.exit(0)
    else:
        for i in range(n, 0, -1):
            value *= i
    return value


fact_number = int(input("Enter the number: "))
print(factorial(fact_number))

# 8. Write a
# program that calculates and prints the value according to the given formula:
# Q = Square root of [(2 * C * D)/H]
# Following are the fixed values of C and H: C is 50. H is 30.
# D  is  the  variable  whose  values  should  be  input  to  your
# program  in  a  comma - separated sequence.
# Example:
# Let  us  assume  the  following  comma  separated  input  sequence  is  given  to  the
# program:
# 100,150,180
# The output of the program should be:
# 18,22,24
sequence = input("Enter comma separated sequence: ")
my_list = sequence.split(',')
for index in my_list:
    print(math.floor(math.sqrt((2 * 50 * int(index)) / 30)), end=',')

# 9. Write a program which takes 2 digits, X,Y as input and generates a 2 - dimensional array.
# The element value in the i-th row and j-th column of the array should be i*j.
# Note: i=0,1.., X-1; j=0,1,¡-Y-1.
# Example:
# Suppose the following inputs are given to the program: 3,5
# Then, the output of the program should be:
# [[0, 0, 0, 0, 0], [0, 1, 2, 3, 4], [0, 2, 4, 6, 8]]
digits = input("Please enter X,Y values: ")
x, y = digits.split(',')
my_list1 = [[i * j for i in range(int(y))] for j in range(int(x))]
print(my_list1)

# 10. Write a program that accepts a comma separated sequence of words as input and
# prints the words in a comma-separated sequence after sorting them alphabetically.
# Suppose the following input is supplied to the program: without,hello,bag,world
# Then, the output should be: bag,hello,without,world
_10List = input("Enter comma separated words: ")
_10List = sorted(_10List.split(','))
_10Str = ','
print(_10Str.join(_10List))

# 11. Write a program that accepts sequence of lines as input and prints the lines after
# making all characters in the sentence capitalized. Suppose the following input
# is supplied to the program:
# Hello world
# Practice makes perfect
# Then, the output should be:
# HELLO WORLD
# PRACTICE MAKES PERFECT
lines = []
no_of_lines = int(input("Enter no of lines:"))
line_no = 0
while True:
    line = input("Enter lines: ")
    lines.append(line.split('\n'))
    line_no += 1
    if line_no == no_of_lines:
        break
lines = sum(lines, [])
for index in (lines):
    print(index.upper())

# 12. Write a program that accepts a sequence of whitespace separated words as input
# and   prints   the   words   after   removing   all   duplicate   words   and   sorting   them
# alphanumerically.
# Suppose the following input is supplied to the program:
# hello world and practice makes perfect and hello world again
# Then, the output should be:
# again and hello makes perfect practice world
_12String = input("Enter white space separated words: ")
_12String = _12String.split(' ')
_12List = []
_12Str = ' '
for index in _12String:
    if index not in _12List:
        _12List.append(index)
print(_12Str.join(sorted(_12List)))

# 13. Write  a  program  which  accepts  a  sequence  of  comma  separated  4  digit  binary
# numbers  as  its  input  and  then  check  whether  they  are  divisible  by  5  or  not.
# The numbers that are divisible by 5 are to be printed in a comma separated sequence.
# Example: 0100,0011,1010,1001
# Then the output should be: 1010
items = []
num = [x for x in input().split(',')]
for p in num:
    x = int(p, 2)
    if not x % 5:
        items.append(p)
print(','.join(items))

# 14. Write  a  program  that  accepts  a  sentence  and  calculate  the  number  of  upper  case
# letters and lower case letters.
# Suppose the following input is supplied to the program:
# Hello world!
# Then, the output should be:
# UPPER CASE 1
# LOWER CASE 9
_14Str = input("Enter sentence with upper lower case: ")
_14UpperCnt = 0
_14LowerCnt = 0
for index in _14Str:
    if index.isupper():
        _14UpperCnt += 1
    if index.islower():
        _14LowerCnt += 1
print("UPPER CASE", _14UpperCnt)
print("LOWER CASE", _14LowerCnt)

# 15. Give example of fsum and sum function of math library.
print(sum([.1, .1, .1, .1, .1, .1, .1, .1, .1, .1]))
print(math.fsum([.1, .1, .1, .1, .1, .1, .1, .1, .1, .1]))