a = int(input("Enter a:"))
b = int(input("Enter b:"))

try:
    print(a*b)
    try:
        print(a/b)
    except:
        print("Inception level exception")
except:
    print("It cannot be done")

print("The END")

try:
    x = int(input("Enter x:"))
    y = 1/x
    print(y)
except ZeroDivisionError:
    print("Cannot divide by zero, Sorry!")
except ValueError:
    print("You have to enter an integer value:")
#except:
    #print("Oh, dear!")
print("This is the END")