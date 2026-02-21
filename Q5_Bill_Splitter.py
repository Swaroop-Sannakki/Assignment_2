#Q5)Create a restaurant bill splitting program. 
#Inputs: Total bill amount, Number of people, Tax percentage, Tip percentage 
#Calculate and Display: Subtotal, Tax amount, Bill after tax, Tip amount, Total bill, Amount per person 


#take all the inputs and store in the variables 
total = float(input("Enter total bill: "))   
No_of_people = int(input("Number of people: "))    
tax = float(input("Tax %: "))                
tip = float(input("Tip %: "))           

tax_amount = total * tax / 100        # Calculate the tax amount from total bill
after_tax = total + tax_amount        # Add tax to total bill
tip_amount = after_tax * tip / 100    # Calculate tip based on amount after tax
final = after_tax + tip_amount        # Add tip to get final total bill
per_person = final / No_of_people        # Divide final bill equally among people

#print all the calculated informations
print("\n=== BILL BREAKDOWN ===")          
print(f"Subtotal: ₹{total:.2f}")        
print(f"Tax: ₹{tax_amount:.2f}")             
print(f"After tax: ₹{after_tax:.2f}")      
print(f"Tip: ₹{tip_amount:.2f}")              
print(f"Total: ₹{final:.2f}")              
print(f"Per person: ₹{per_person:.2f}")    