def parking(n):
    if n <= 2:
        print(100)
    elif n <= 5:
        print(300)
    else:
        print(500)


n = int(input())
parking(n)