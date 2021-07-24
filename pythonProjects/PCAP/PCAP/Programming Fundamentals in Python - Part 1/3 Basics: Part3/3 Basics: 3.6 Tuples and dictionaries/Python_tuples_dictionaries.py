tuple1 = (1, 2, 3, 4)
tuple2 = .1, .2, .3, .4

print(tuple1)
print(tuple2)

emptytuple = ()
print(emptytuple)

oneelementtuple = (1,)
print(oneelementtuple)

# tuple reading would be like list only
tuple = (1, 10, 100, 1000)

print(tuple[0])
print(tuple[-1])
print(tuple[1:])
print(tuple[:-2])

for el in tuple:
    print(el)

# concatenating tuples
tuple1 = (1, 10, 100, 1000)
tuple2 = (0,)

print(tuple1 + tuple2)

# how to use tuple
tuple = (1, 10, 100)
t1 = tuple + (1000, 10000)
t2 = tuple * 3

print(t1)
print(t2)
print(10 in tuple)
print(-10 not in tuple)

# dictionary
dct = {'cat': 'chat', 'dog': 'chien', 'horse': 'cheval'}
phones = {'boss': 5551234567, 'Suzy': 5557654321}
empty = {}

print(dct['cat'])
print(phones['Suzy'])
print(empty)

# how to use a dictionary
dct = {'cat': 'chat', 'dog': 'chien', 'horse': 'cheval'}
words = ['cat', 'lion', 'horse']

for word in words:
    if word in dct:
        print(word, "->", dct[word])
    else:
        print("Not in dictionary", word)

# using keys() method
for key in dct.keys():
    print(key, "->", dct[key])

# using sorted in keys() method
for key in sorted(dct.keys()):
    print(key, "->", dct[key])

# using items() method
for key, value in sorted(dct.items()):
    print("key is:", key)
    print("value is:", value)

# using values() method
for value in sorted(dct.values()):
    print(value)

# assigning new value to an existing key
dct['cat'] = 'minou'
print(dct)

# assigning new key value pair
dct['lion'] = 'lion'
print(dct)

# to remove a key from dictionary
del dct['dog']
print(dct)
