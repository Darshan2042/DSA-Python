#  Check if a number is perfect number. 

def prime_number(n):
    sum_div = 0
    for i in range(1,n):
        if n % i == 0:
            sum_div += i

    return sum_div == n

def prime_number_range(start , end):
    for num in range(start , end+1):
        if prime_number(num):
            print(num , end= " ")

prime_number_range(1,1000)