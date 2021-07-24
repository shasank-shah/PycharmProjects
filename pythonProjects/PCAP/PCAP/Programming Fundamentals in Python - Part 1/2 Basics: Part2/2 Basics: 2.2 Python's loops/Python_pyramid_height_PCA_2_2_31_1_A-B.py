blocks = int(input("Enter number of blocks:"))
height = 0
inlayer = 1

if blocks <= 0:
    print("No of blocks cannot be 0 or negative!")
else:
    while inlayer <= blocks:
        height += 1
        blocks -= inlayer
        inlayer += 1

print("Height of pyramid: ", height)
