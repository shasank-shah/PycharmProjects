max = -99999
number = float(input('Enter number:'))

while number != -1:
    if number > max:
        max = number

    number = int(input('Enter value or -1 to stop: '))

print("The largest number is", max)
