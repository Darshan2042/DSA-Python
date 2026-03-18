# Leap Year or not.

def leap_year(n):
    if (n % 400 ==0) or (n % 4 == 0 and n % 100 != 0):
        return "Leap Year"
    else:
        return "Non Leap Year"
    
n = 1900
print(leap_year(n))