def even_odd(n):
    if n % 2 == 0:
        print("even")
    else:
        print("odd")
while True:
    n = int(input("Enter Number: "))
    ans = even_odd(n)