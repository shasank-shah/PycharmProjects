numbers = [111, 7, 2, 1]
numbers.append(4)  # list method "append"
print(len(numbers))
print(numbers)

numbers.insert(0, 222)  # list method "insert" to add first element
numbers.insert(2, 333)  # list method "insert" to add third element
print(numbers)

a = numbers[1]
numbers[1] = numbers[0]
numbers[0] = a

print(numbers)

empty_list = []  # emply list without elements
for i in range(5):
    empty_list.append(i + 1)  # adding elements using append method
print(empty_list)

empty_list = []  # empty list without elements
for i in range(5):
    empty_list.insert(0, i + 1)  # adding elements using insert method which should have starting index position
print(empty_list)

new_list = [10, 1, 8, 3, 5]
sum = 0
for i in range(len(new_list)):
    sum += new_list[i]
print(sum)

new_list = [10, 1, 8, 3, 5]
sum = 0
for i in new_list:
    sum += i
print(sum)

# swapping values without extra variable
variable1 = 1
variable2 = 2

print("Before swapping, variable1 = ", variable1, " and variable2 = ", variable2)

variable1, variable2 = variable2, variable1  # Swapping logic

print("After swapping, variable1 = ", variable1, " and variable2 = ", variable2)

my_list = [10, 1, 8, 3, 5]
my_list[0], my_list[4] = my_list[4], my_list[0]
my_list[1], my_list[3] = my_list[3], my_list[1]
print(my_list)

# Using for loop for swapping
my_list = [10, 1, 8, 3, 5]
l = len(my_list)
for i in range(l // 2):
    my_list[i], my_list[l - i - 1] = my_list[l - i - 1], my_list[i]

print(my_list)
