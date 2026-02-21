from datetime import date   # Imports the date class from datetime module to work with dates

# user inputs are taken i.e day , month, year in integer format
day = int(input("Enter birth day (1-31): "))     
month = int(input("Enter birth month (1-12): ")) 
year = int(input("Enter birth year: "))          

birth_date = date(year, month, day)  # Create a date object using entered year, month, and day

today = date.today()  # Get today's current date from system

age_years = today.year - birth_date.year  # Calculate rough age by subtracting birth year from current year

# Check if birthday has not happened yet this year
if (today.month, today.day) < (birth_date.month, birth_date.day):  
    age_years -= 1  # If birthday not reached yet, reduce age by 1

days_lived = (today - birth_date).days  # Calculate total number of days lived by subtracting dates

months_lived = days_lived // 30  # calculates approximate months lived by dividing days by 30
hours_lived = days_lived * 24    # Convert days lived into hours
minutes_lived = hours_lived * 60 # Convert hours lived into minutes

print("\n AGE DETAILS")          
print("Years:", age_years)         
print("Months:", months_lived)     
print("Days:", days_lived)         
print("Hours:", hours_lived)       
print("Minutes:", minutes_lived)   
print("Years until 100:", 100 - age_years)  