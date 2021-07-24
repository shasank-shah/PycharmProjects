secret_number = 8

print(
    "Welcome to my game, muggle!\nEnter an integer number and guess what number I've picked for you!\nI'll give you a hint: it's an integer number from 0 to 10.")

number = int(input("Enter number:"))

# Write your while loop and the rest of your code here
while number != secret_number:
    print("No, that's not the number I've picked for you. Try again!")
    number = int(input("Enter number:"))

print(secret_number, "Well done! That's the number I've chosen for you! You are free now.")
