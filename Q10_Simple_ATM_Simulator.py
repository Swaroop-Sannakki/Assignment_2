#Create an ATM simulation with initial balance = ₹10,000. 
#Menu: 1. Check Balance  2. Deposit Money  3. Withdraw Money  4. Exit 
#Rules: - Check sufficient balance before withdrawal - Minimum balance of ₹500 must remain at all times - Display transaction messages and updated balance after each transaction


balance = 10000  # Set initial bank account balance to 10000

while True:  # Start infinite loop so ATM menu keeps showing till the user exit 
    print("\n1.Check 2.Deposit 3.Withdraw 4.Exit")  # Display ATM options for the user 
    ch = input("Choice: ")  # takes input from the user  to choose an option

    if ch == "1":  # If user selects Check Balance
        print("Balance:", balance)  # shows current balance

    elif ch == "2":  # If user selects Deposit option
        amount = float(input("Deposit: "))  # Ask deposit amount
        balance += amount
        print("Deposition successfull..")
        print("New Balance:",balance)# Add deposit amount to balance
        

    elif ch == "3":  # If user selects Withdraw
        amount = float(input("Enter amount to Withdraw: "))  # Ask withdrawal amount
        
        # Check if minimum balance of 500 will remain after withdrawal
        if balance - amount >= 500:
            balance -= amount
            print("withdrwa successfull...!!")
            print("New Balance:",balance)# subtract amount from balance
        else:
            print("Minimum balance required")  # Warn if balance would go below 500

    elif ch == "4":  # If user selects Exit
        break  # Stop loop and end ATM program