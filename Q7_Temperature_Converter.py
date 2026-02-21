#Q7) Create a temperature converter with a menu-based system supporting: 
#1. Celsius to Fahrenheit   2. Fahrenheit to Celsius   3. Celsius to Kelvin   4. Kelvin to Celsius   5. Fahrenheit to Kelvin   6. Kelvin to Fahrenheit   7. Exit 

#i use while loop and if else for this problem since many sub questions are present and we can get them individually by taking the condition in while looop

while True:  # Start an infinite while loop so program keeps running until user exits (i.e true)
    print("\n1.C→F 2.F→C 3.C→K 4.K→C 5.F→K 6.K→F 7.Exit")  # it Shows conversion menu 
    ch = input("Choice: ")  # it asks user to choose conversion option and store it in variable ch

    if ch == "7":  # If user selects 7 then  Exit the loop and stop the program
        break  

    temp = float(input("Enter temperature value: "))  # take the input of  temperature value and convert to decimal

    if ch == "1":  # Celsius to Fahrenheit
        print("celcius to fahrenheit")
        print((temp * 9 / 5) + 32)  # C→F formula applied5
    elif ch == "2":  # Fahrenheit to Celsius
        print("Fahrenheit to Celsius")
        print((temp - 32) * 5 / 9)  # Apply F→C formula
    elif ch == "3":  # Celsius to Kelvin
        print("Celsius to Kelvin")
        print(temp + 273.15)  # Apply C→K formula
    elif ch == "4":  # Kelvin to Celsius
        print("Kelvin to Celsius")
        print(temp - 273.15)  # Apply K→C formula
    elif ch == "5":  # Fahrenheit to Kelvin
        print("Fahrenheit to Kelvin")
        print((temp - 32) * 5 / 9 + 273.15)  # Convert F→C then C→K4
    elif ch == "6":  # Kelvin to Fahrenheit
        print("Kelvin to Fahrenheit")
        print((temp - 273.15) * 9 / 5 + 32)  # Convert K→C then C→F