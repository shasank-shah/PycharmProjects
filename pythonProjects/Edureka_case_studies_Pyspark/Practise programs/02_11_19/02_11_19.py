'''
str1 = 'Hello'
print(id(str1), str1)
str1 = 'hello'
print(id(str1), str1)
'''

'''
string = 'hello world'
string[0] = 'b'
print(string)
'''

'''
string = 'hello world'
print(string[::-1])
'''

tuple1 = ('a', 'b', 'c')
tuple2 = (0,) + tuple1
print(type(tuple2), tuple2)

# To use max and min function in tuple, the elements of it has to be same data type
tuple3 = ('shell', 'del', 'val')
print(sorted(tuple3))

tuple4 = tuple3 + ('', 'last')
print(tuple4)

print(type(tuple2[0]))

list = [1, 2.05, 'stringElement']
print(id(list), ': ', list)
list[2]='elementInString'
print(id(list), ': ', list)
