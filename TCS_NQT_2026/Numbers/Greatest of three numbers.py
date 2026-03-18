# Greatest of three numbers.

def greatest_of_three_number(a,b,c):
    if a >= b and a >=c:
        return "A is Greater"
    elif b >= a and b >= c:
        return "B is Greater"
    else:
        return "C is Greater"
    

a = 50
b = 20
c = 5
print(greatest_of_three_number(a,b,c))