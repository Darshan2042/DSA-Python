# def bill2(unit):
#     if unit < 100:
#         bill = 0
#     elif unit <= 200:
#         rem = unit - 100
#         bill = rem * 5
#     elif unit <= 300:
#         rem = unit - 100  
#         rem2 = rem - 100    
#         bill = (rem - rem2) * 5 + rem2 * 7
#     else:
#         rem = unit - 100
#         rem2 = rem - 100
#         rem3 = rem2 - 100
#         bill = (rem - rem2) * 5 + (rem2 - rem3) * 7 + rem3 * 10
#     return bill

# unit = int(input("Enter unit: "))
# print("Bill Amount:", bill2(unit))

def is_leap(year):
    leap = False

    if (year % 4 == 0 and year % 100 == 0) and (year % 400 == 0):
        leap = True
    
    return leap

year = int(input())
print(is_leap(year))