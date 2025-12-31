while True:
    choice = input("Enter The Day: ")
    match choice:
        case "sunday" | "saturday":
            print("Weekend")
        case _:
            print("Weekdays")
