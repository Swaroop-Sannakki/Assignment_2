balance = 10000  # Initial balance ₹10,000

while True:  # Run ATM until user exits
    print("\n=== ATM MENU ===")
    print("1. Check Balance")
    print("2. Deposit Money")
    print("3. Withdraw Money")
    print("4. Exit")

    ch = input("Enter choice: ")  # User selects option

    if ch == "1":  # Check balance
        print("Current Balance: ₹", balance)

    elif ch == "2":  # Deposit
        amount = float(input("Enter deposit amount: "))
        balance += amount
        print("Deposit successful!")
        print("Updated Balance: ₹", balance)

    elif ch == "3":  # Withdraw
        amount = float(input("Enter withdrawal amount: "))

        # Check sufficient balance & minimum ₹500 rule
        if amount > balance:
            print("Insufficient balance!")
        elif balance - amount < 500:
            print("Minimum balance ₹500 must remain!")
        else:
            balance -= amount
            print("Withdrawal successful!")
            print("Updated Balance: ₹", balance)

    elif ch == "4":  # Exit
        print("Thank you for using ATM.")
        break

    else:
        print("Invalid choice. Try again.")