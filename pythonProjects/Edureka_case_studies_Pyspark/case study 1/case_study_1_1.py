import sys
from time import gmtime, strftime
import math
from random import randrange, randint

# 1. What is the output of the following code?
# nums = set([1,1,2,3,3,3,4,4])
# print (len(nums))
# Hint: Set consists unique element.
nums = set([1, 1, 2, 3, 3, 3, 4, 4])
print(len(nums))  # 4

# 2. What will be the output?
d = {"john": 40, "peter": 45}
print(list(d.keys()))  # ['john', 'peter']

# 3. A website requires a user to input username and password to register. Write a program
# to check the validity of password given by user. Following are the criteria for checking password:
# 1. At least 1 letter between [a-z]
# 2. At least 1 number between [0-9]
# 3. At least 1 letter between [A-Z]
# 4. At least 1 character from [$#@]
# 5. Minimum length of transaction password: 6
# 6. Maximum length of transaction password: 12
_3InputPassword = input("Enter password: ")
_3Password = []
if len(_3InputPassword) < 6:
    print("Minimum length of password should 6")
    sys.exit(0)
if len(_3InputPassword) > 12:
    print("Maximum length of password should 12")
    sys.exit(0)
for index in _3InputPassword:
    _3Password.append(index)
print(_3Password)

# 4. Write a for loop that prints all elements of a list and their position in the list.
a = [4, 7, 3, 2, 5, 9]
for index in range(len(a)):
    print("index is: ", index, " and element is: ", a[index])

# 5. Please   write   a   program   which   accepts  a   string   from   console   and   print   the
# characters that have even indexes.
# Example: If the following string is given as input to the program:
# H1e2l3l4o5w6o7r8l9d
# Then, the output of the program should be:
# Helloworld
_5Input = input("Enter string: ")
_5List = list(_5Input)
_5OutputList = []
_5OutputList.append(_5List[0])
_5Output = ''
for index in range(1, len(_5List)):
    if (index % 2 == 0):
        _5OutputList.append(_5List[index])
print(_5Output.join(_5OutputList))

# 6. Please write a program which accepts a string from console and print it in reverse order.
# Example: If the following string is given as input to the program:
# rise to vote sir
# Then, the output of the program should be:
# ris etov ot esir
_6Output = ''
_6String = list(input("Please enter string to be reversed: "))
print(_6Output.join(_6String[::-1]))

# 7. Please write a program which count and print the numbers of each character in a string input by console.
# Example: If the following string is given as input to the program:
# abcdefgabc
# Then, the output of the program should be:
# a,2
# c,2
# b,2
# e,1
# d,1
# g,1
# f,1
def _7Duplicates(_7StringInput):
    _7StringSize = len(_7StringInput)
    _7StringDict = {}
    for i_index in range(_7StringSize):
        _7StringTemp = i_index + 1
        count = 1
        for j_index in range(_7StringTemp, _7StringSize):
            if _7StringInput[i_index] == _7StringInput[j_index]:
                count += 1
                print("i_index: ", i_index, "j_index: ", j_index, "count: ", count)
                _7StringDict[_7StringInput[i_index]] = count
                #_7StringDict.update({_7StringInput[i_index]: count})
            #if _7StringInput[i_index] != _7StringInput[j_index]:
            else:
                print("i_index: ", i_index, "j_index: ", j_index, "count: ", count)
                _7StringDict[_7StringInput[i_index]] = count
                #_7StringDict.update({_7StringInput[i_index]: count})
    for _7Element, _7Value in _7StringDict.items():
        print(_7Element, _7Value)
_7StringInput = list(input("Enter characters: "))
_7Duplicates(_7StringInput)

# 8. With   two   given   lists   [1,3,6,78,35,55]   and   [12,24,35,24,88,120,155],   write   a
# program to make a list whose elements are intersection of the above given lists.
_8List1 = [1, 3, 6, 78, 35, 55]
_8List2 = [12, 24, 35, 24, 88, 120, 155]
print(set(_8List1).intersection((set(_8List2))))

# 9. With a given list [12,24,35,24,88,120,155,88,120,155], write a program to print this
# list after removing all duplicate values with original order reserved
_9List =  [12, 24, 35, 24, 88, 120, 155, 88, 120, 155]
_9ListSize = len(_9List)
_9TempList = []
for i_index in range(_9ListSize):
    _9Temp = i_index + 1
    for j_index in range(_9Temp, _9ListSize):
        if _9List[i_index] == _9List[j_index]:
            _9TempList.append(_9List[i_index])
print(_9List)
_9ReversedList = _9List[::-1]
print(_9ReversedList)
print(_9TempList)
for i_index in range(len(_9TempList)):
    for j_index in range(len(_9ReversedList)):
        if _9ReversedList[j_index] == _9TempList[i_index]:
            _9ReversedList.remove(_9ReversedList[j_index])
            #print(j_index)
            break
print("After deleting: ", _9ReversedList[::-1])

# 10. By using list comprehension, please write a program to print the list after removing
# the value 24 in [12,24,35,24,88,120,155].
_10List = [12,24,35,24,88,120,155]
[_10List.remove(ele) for ele in _10List if ele == 24]
print(_10List)

# 11. By using list comprehension, please write a program to print the list after removing
# the 0th,4th,5th numbers in [12,24,35,70,88,120,155].
_11List = [12,24,35,70,88,120,155]
_11Result = []
[_11Result.append(_11List[index]) for index in range(len(_11List)) if index not in (0, 4, 5)]
del _11List
print(_11Result)

# 12. By using list comprehension, please write a program to print the list after removing
# delete numbers which are divisible by 5 and 7 in [12,24,35,70,88,120,155].
_12List = [12,24,35,70,88,120,155]
_12Result = []
[_12Result.append(ele) for ele in _12List if ((ele % 5 != 0) or (ele % 7 != 0))]
del _12Result
print(_12Result)

# 13. Please  write  a  program  to  randomly  generate  a  list  with  5  numbers,  which  are
# divisible by 5 and 7 , between 1 and 1000 inclusive.
_13Count = 1
_13List = []
while True:
    _13RandomNumber = randrange(1, 1001)
    if ((_13RandomNumber % 5 == 0) and (_13RandomNumber % 7 == 0)):
        _13List.append(_13RandomNumber)
        _13Count += 1
    if (_13Count >= 6):
        break
print(_13List)

# 14. Write  a  program  to  compute  1/2+2/3+3/4+...+n/n+1  with  a  given  n  input  by
# console (n>0).
# Example:
# If the following n is given as input to the program:
# 5
# Then, the output of the program should be:
# 3.55
_14Result = 0
_14Input = int(input("Please Enter n value greater than 0: "))
for index in range(_14Input + 1):
    _14Result += (index/(index + 1))
print("{:.2f}".format(_14Result))