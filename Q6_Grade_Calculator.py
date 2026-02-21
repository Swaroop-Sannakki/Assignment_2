#Ask users for marks in 5 subjects (out of 100 each). Calculate and display: 
#1. Marks in each subject   2. Total marks (out of 500)   3. Percentage   4. Grade   5. Result: Pass/Fail (Pass if all subjects >= 40)

marks = []  # Create an empty list to store marks of 5 subjects

for i in range(1,6):  # iterate Loop from 1 to 5 (for 5 subjects)
    m = float(input(f"Enter marks for subject {i}: "))  # take input  marks for each subject and convert to decimal number
    marks.append(m)  # append() adds or pushes entered marks into the marks list

total = sum(marks)  # Add all marks in the list to get total marks
percent = total/500*100  # Calculate percentage assuming each subject is out of 100 (total 500)

#use if else condition statement to check pass or fail
if all(m>=40 for m in marks):  # all() Checks if every subject mark is at least 40
    result = "Pass"  # If all subjects >=40, student passes
else:
    result = "Fail"  # If any subject <40, student fails

#use nested else if conditional statements to assign grades based on their percentage
if percent>=90:      # If percentage is 90 or above ,Assign grade A+
    grade="A+"       
elif percent>=80:    # If percentage is 80–89,assign grade A
    grade="A"        
elif percent>=70:    # If percentage is 70–79, assign grade B
    grade="B"     
elif percent>=60:    # If percentage is 60–69 ,assign grade C
    grade="C"        
elif percent>=50:    # If percentage is 50–59,assign grade D
    grade="D"        
else:                # If percentage below 50, assign fail grade F
    grade="F"        

#print or display all calculated information
print("Total:", total)         
print("Percentage:", percent)   
print("Grade:", grade)          
print("Result:", result)       