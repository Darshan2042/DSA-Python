def gym_membership(n):
    if n <= 0:
        return "Invalid Input"
    elif n <= 1:
        return "Cost: 2000"
    elif n <= 3:
        return " Cost: 3000"
    elif n <= 6:
        return " Cost: 5000"
    elif n <= 9:
        return "Cost: 9000"
    elif n <= 12:
        return "Cost: 15000"
    
n = int(input("Enter the Month: "))
print(gym_membership(n))