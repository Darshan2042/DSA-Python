def print_number(n):
    if n == 0:
        return 
    print(n)
    print_number(n-1)

print(print_number(100)) 

n = 4 
for i in range(1,n+1):
     print("#" * i)
for i in range(n-1,0,-1):
    print("#" * i )