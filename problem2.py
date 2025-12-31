choice = int(input("Enter Day: "))
day = choice % 7
match day:
    case 0:
        print("Weekend")
    case 6: 
        print("Weekend")
    case _: 
        print("Weekday")
