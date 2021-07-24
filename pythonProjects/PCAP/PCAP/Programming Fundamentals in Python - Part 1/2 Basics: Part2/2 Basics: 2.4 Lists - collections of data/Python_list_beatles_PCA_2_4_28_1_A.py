# step 1
Beatles = []
print("Step 1:", Beatles)

# step 2
Beatles.append("John Lennon")
Beatles.append("Paul McCartney")
Beatles.append("George Harrison")
print("Step 2:", Beatles)

# step 3
for i in range(4, 6):
    # band_member_name = input("Enter band member name: ")
    Beatles.append(input("Enter band member name: "))
print("Step 3:", Beatles)

# step 4
del Beatles[-1]
del Beatles[-1]
print("Step 4:", Beatles)

# step 5
Beatles.insert(0, "Ringo Starr")
print("Step 5:", Beatles)

print("The Fab", len(Beatles))
