# We can have list inside in a tuple
tuple = (1, 2, [3, 4.5, 'element1'], 5, 6.6, 'element2')
print(tuple)

# We can have tuple inside in a list
list1 = [1, 2, 3, (4, 5.5, 'element1'), 6, 7.5, 'element2']
print(list1)

# dictionary
dictionary = {'bannana': 20, 'apple': 50, 'orange': 60, 'cherry': 80}
print(dictionary)

# dictionary inside an dictionary
dictionary = {'bananna': 20, 'apple': {'himachali': 45, 'kashmiri': 40}, 'orange': 60, 'cherry': 80}
print(dictionary)

# storing dictionary keys in a list
list2 = list(dictionary.keys())
print(list2)

# storing dictionary values in a list
list3 = list(dictionary.values())
print(list3)

# set can store only distinct values
set1 = {1, 2, 2, 3, 4, 5}
print(set1)

# converting set to a list
set2 = {1, 2, 3, 4, 5}
list4 = list(set2)
print(list4)

# if, elif and else statement

# while loop
i = 0
while i < 20:
    print(i, end=' ')
    i += 1

# for loop

# break, continue, pass statements

# file operations such as write, read
    # tell method will tell the cursor position
    # seek method will place the cursor in particular position

#https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files
#https://docs.python.org/3/library/
#gaurav.sharma@edureka.co
