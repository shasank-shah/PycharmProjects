lottery = [3, 7, 11, 42, 34, 49]
drawn = [5, 11, 9, 42, 3, 49]
hits = 0

for number in lottery:
    if number in drawn:
        hits += 1

print("hits: ", hits)

# Select duplicate elements
list = [3, 7, 11, 42, 34, 49, 7, 11]
new_list = []
found = True

for i in range(len(list) - 1):
    print("i value: ", list[i], "i+1 value: ", list[i + 1])

'''
for i in range(len(list)-1):
    for j in range(len(list)-1):
        print("i value: ", list[i], "j value: ", list[j+1])
'''
for i in range(len(list) - 1):
    for j in range(i + 1, len(list)):
        if list[i] == list[j]:
            new_list.append(list[i])
            print("i value: ", list[i], "j value: ", list[j])
print("new list: ", new_list)

for number in new_list:
    if number in list:
        list.remove(number)

print("\nlist with unique elements are: ", list)

# deleting new_list
del new_list

# testing list remove method
list = [1, 2, 2, 2, 3]
list.remove(2)
print("remove method: ", list)
