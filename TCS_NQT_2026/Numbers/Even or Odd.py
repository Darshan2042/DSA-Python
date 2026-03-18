# Even or Odd.

def even_odd(n):
    if n % 2 == 0:
        return "Even"
    else:
        return "Odd"
    
def even_odd_range(start,end):
    for num in range(start,end+1):
        if even_odd(num):
            print(num , end= " ")

even_odd_range(1,100)