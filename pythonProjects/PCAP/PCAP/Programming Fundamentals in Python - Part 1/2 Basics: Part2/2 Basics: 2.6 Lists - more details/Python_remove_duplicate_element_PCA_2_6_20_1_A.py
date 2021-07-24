list = [1, 2, 4, 4, 1, 4, 2, 6, 2, 9]
new_list = []
#
for number in list:
    if number not in new_list:
        new_list.append(number)
print("new list: ", new_list)
list = new_list[:]
print("list: ", list)
del new_list
exit()
