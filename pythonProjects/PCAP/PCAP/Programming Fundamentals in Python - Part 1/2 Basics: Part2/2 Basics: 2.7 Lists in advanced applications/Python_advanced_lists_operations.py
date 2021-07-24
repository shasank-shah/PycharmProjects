row = []
for i in range(8):
    row.append("WHITE_PAWN")

print(row)

# list comprehension

row = [1 for i in range(8)]
print(row)

board = [[1 for i in range(8)] for j in range(8)]
print(board)

temps = [[0.0 for h in range(24)] for d in range(31)]
sum = 0.0
for day in temps:
    sum += day[11]
average = sum / 31
print("Average temperature at noon: ", average)
