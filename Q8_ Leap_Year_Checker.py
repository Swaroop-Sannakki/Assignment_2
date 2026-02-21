#Q7) Create a program that checks if a year is a leap year. 

year = int(input("Enter year: "))  # takes input from user to enter a year and convert it to integer

# to Check leap year condition i use if else condition

if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):  # apply condition: divisible by 4 AND (not divisible by 100 OR divisible by 400)
    print(year, "is leap year because it is divisible by 4 and not divisible 100 or divisible by 400")# If condition true - leap year
else:
    print(year, "not leap year since it is not divisible by 4")  # else - not leap year