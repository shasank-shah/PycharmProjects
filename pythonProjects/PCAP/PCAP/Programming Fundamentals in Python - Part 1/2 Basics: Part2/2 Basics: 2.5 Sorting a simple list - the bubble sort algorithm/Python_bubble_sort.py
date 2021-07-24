my_list = [8, 10, 6, 2, 4]
print("Length of list: ", len(my_list), "\n")

print("\nlist indexes:")
for i in range(len(my_list)):
    print(i, my_list[i])

print("\nBefore sorting:")
for i in range(len(my_list)):
    print(my_list[i], end=' ')

print("\nLength of list -1: ", len(my_list) - 1)
print("\nAfter sorting:")

list = []
swapped = True
num = int(input("How many elements do you want to sort:"))
for i in range(num):
    val = int(input("Enter Element:"))
    list.append(val)
print("Unsorted list:\n", list)

while swapped:
    swapped = False
    for i in range(len(list) - 1):
        if list[i] > list[i + 1]:
            swapped = True
            list[i], list[i + 1] = list[i + 1], list[i]
print("\nSorted: ")
print(list, end=' ')

# using sort method

list = [8, 10, 6, 2, 4]
list.sort()
print("Using sort method: ", list)
