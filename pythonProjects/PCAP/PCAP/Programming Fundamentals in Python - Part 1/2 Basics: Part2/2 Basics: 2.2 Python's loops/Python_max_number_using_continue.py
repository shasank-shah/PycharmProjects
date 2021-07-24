max = -999999
counter = 0
number = int(input("Enter a value: "))

while number != -1:
    if number == -1:
        continue
    counter += 1
    if number > max:
        max = number
    number = int(input("Enter a value: "))

if counter:
    print("The max number is: ", max)
else:
    print("Are you kidding, you have not entered any value")
