list1 = [1]
list2 = list1
list1[0] = 2
print(list2)

# List with slices
list1 = [1]
list2 = list1[:]
list1[0] = 2
print(list2)

list = [10, 8, 6, 4, 2]
new_list = list[1:3]
print(new_list)

list = [10, 8, 6, 4, 2]
new_list = list[1:-1]
print(new_list)

list = [10, 8, 6, 4, 2]
del list[1:3]
print(list)

list = [10, 8, 6, 4, 2]
del list[:]
print(list)

list = [10, 8, 6, 4, 2]
del list
print(list)

list = [0, 3, 12, 8, 2]
print(5 in list)
print(5 not in list)
print(12 in list)

list = [0, 3, 11, 5, 1, 9, 7, 15, 13]
max = list[0]
for i in range(1, len(list)):
    if max < list[i]:
        max = list[i]
print("Max: ", max)

list = [0, 3, 11, 5, 1, 9, 7, 5000, 15, 13, 548, 4345]
max = list[0]
for i in list[1:]:
    if i > max:
        max = i
print("Again max:", max)

list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
toFind = 5
found = False
for i in range(len(list)):
    found = list[i] == toFind
    if found:
        break

if found:
    print("Element found in index: ", i)
else:
    print("absent")
