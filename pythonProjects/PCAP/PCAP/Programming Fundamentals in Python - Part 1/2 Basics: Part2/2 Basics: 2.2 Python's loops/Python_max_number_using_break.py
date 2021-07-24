max = -99999
counter = 0

while True:
    number = int(input("Enter number: "))
    if number == -1:
        break
    counter += 1
    if number > max:
        max = number
if counter:
    print("The largest number is", max)
else:
    print("Are you kidding, you have not entered any value")
