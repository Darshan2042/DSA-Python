row = 6

# for i in range(row):
#     for j in range(row- 1,-1,-1):
#         print("*",end="")
#     print()

for i in range(row):
    for j in range(row - i - 1):
        print(" ", end="")
    for k in range(2 * i + 1):
        print("*", end="")
    print()