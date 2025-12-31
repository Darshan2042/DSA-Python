def max(a, b, c):
    if a > b:
        if a > c:
            print("A is Greater")
        else:
            print("C is Greater")
    else:
        if b > c:
            print("B is Greater")
        else:
            print("C is Greater")
a = 20
b = 10
c = 5
max(a, b, c)
