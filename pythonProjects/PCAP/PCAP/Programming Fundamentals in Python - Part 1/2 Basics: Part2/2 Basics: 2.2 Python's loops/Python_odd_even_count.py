odd = 0
even = 0
number = int(input("Enter number:"))

while number != 0:
    if number % 2 == 0:
        even += 1
    else:
        odd += 1
    number = int(input("Enter 0 to exit"))

print("Odd Count: ", odd)
print("Even Count: ", even)
