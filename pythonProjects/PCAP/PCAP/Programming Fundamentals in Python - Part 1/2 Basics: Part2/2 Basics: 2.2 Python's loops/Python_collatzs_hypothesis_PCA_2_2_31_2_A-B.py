c0 = int(input("Enter non-negative or non-zero integer:"))

if c0 > 1:
    steps = 0
    while c0 != 1:
        if c0 % 2 == 0:
            c0 = c0 // 2
        else:
            c0 = 3 * c0 + 1
        steps += 1
        print(c0, end=' ')
    print("steps = ", steps)
else:
    print("Bad c0 value")
