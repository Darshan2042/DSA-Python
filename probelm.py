chai = 0
coffee = 0
pizza = 0

while True:
    print("MENU ")
    print("1. Chai (₹10)")
    print("2. Coffee(₹20)")
    print("3. Pizza (₹100)")
    print("4. Exit & Show Bill")
    choice = int(input("Enter your choice: "))

    match choice:
        case 1:
            chai += 1
            print("Chai added")
        case 2:
            coffee += 1
            print("Coffee added")
        case 3:
            pizza += 1
            print("Pizza added")
        case 4:
            break
        case _:
            print("Invalid choice. Try again.")


total = chai * 10 + coffee * 20 + pizza * 100
print("Dolly Chai wala")
print("\n--- BILL ---")
print("Item\t\tQty\tPrice\tTotal")
print(f"Chai\t\t{chai}\t₹10\t₹{chai*10}")
print(f"Coffee\t\t{coffee}\t₹20\t₹{coffee*20}")
print(f"Pizza\t\t{pizza}\t₹100\t₹{pizza*100}")
print(f"TOTAL:\t\t\t\t₹{total}")


