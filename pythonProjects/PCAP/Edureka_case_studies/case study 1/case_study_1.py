import re

# 1. what is the output of the following code
nums = set([1, 1, 2, 3, 3, 3, 4, 4])
print(len(nums))
# Ans : 4

# 2. what will be the output?
d = {"john":"40", "peter":"45"}
print(list(d.keys()))
# Ans : ['john', 'peter']

# 3. A website requires a user to input username and password to register. Write a program to check the validity of password given by user. Following are the criteria for checking password:
# 1. At least 1 letter between [a-z]
# 2. At least 1 number between [0-9]1.
# 3. At least 1 letter between [A-Z]
# 4. At least 1 character from [$#@]
# 5. Minimum length of transaction password:
# 6. Maximum length of transaction password: 12

username = input("Enter user name: ")
password = input("Enter password: ")
print("The username is: ", username)
if len(password) < 6:
    print("Password cannot be less than 6 characters")
elif len(password) > 12:
    print("Password cannot be greater than 12 characters")
else:
    if (password.isalnum() or re.findall("[$#@]", password)):
        print("The password is: ", password)
    else:
        print("Password does not satisfy the requirement.")

# 4. Write a for loop that prints all elements of a list and their position in the list.
a = [4,7,3,2,5,9]
for indx in range(len(a)):
    print("Position-> ", indx, "Element-> ", a[indx])

# 5. Please   write   a   program   which   accepts  a   string   from   console   and   print   the characters that have even indexes.
string = input("The string is: ")
for indx in range(len(string)):
    if indx == 0 or indx % 2 == 0:
        print(string[indx], end='')
    else:
        pass

# 6. Please write a program which accepts a string from console and print it in reverse order.
string = input("Enter the string: ")
for indx in reversed(range(len(string))):
    print(string[indx], end='')

# 7. Please write a program which count and print the numbers of each character in a string input by console.

# 8. With   two   given   lists   [1,3,6,78,35,55]   and   [12,24,35,24,88,120,155],   write   a program to make a list whose elements are intersection of the above given lists.
list1 = [1,3,6,78,35,55]
list2 =  [12,24,35,24,88,120,155]
list = []
for i in range(len(list1)):
    if list1[i] in list2:
        list.append(list1[i])

print(list)

# 9. With a given list [12,24,35,24,88,120,155,88,120,155], write a program to print this list after removing all duplicate values with original order reserved
mylist = [12,24,35,24,88,120,155,88,120,155]
mylist = list(dict.fromkeys(mylist))
print(mylist)

# 10. By using list comprehension, please write a program to print the list after removing the value 24 in [12,24,35,24,88,120,155]
mylist = [12,24,35,24,88,120,155]
list = []
for i in range(len(mylist)):
    if mylist[i] == 24:
        pass
    else:
        list.append(mylist[i])

print(list)

# 11. By using list comprehension, please write a program to print the list after removing the 0th,4th,5th numbers in [12,24,35,70,88,120,155]
mylist = [12,24,35,70,88,120,155]
list = []
for i in range(len(mylist)):
    if i in (0, 4, 5):
        pass
    else:
        list.append(mylist[i])

print(list)


