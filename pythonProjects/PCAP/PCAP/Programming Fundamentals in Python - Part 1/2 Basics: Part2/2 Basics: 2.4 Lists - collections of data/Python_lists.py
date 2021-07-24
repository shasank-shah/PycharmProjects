numbers = [10, 5, 7, 2, 1]
print(numbers)

numbers[0] = 111
print(numbers)

numbers[1] = numbers[4]
print(numbers)

print(numbers[0])

del numbers[0]
print(len(numbers))
print(numbers)

print(numbers[-1])
