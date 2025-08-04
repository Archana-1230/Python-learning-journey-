#Write a program to check if a person is eligible for scholarship (above 85% marks + annual income below ₹2 lakh)
# Check if a person is eligible for scholarship
mark = int(input("Enter your marks (%): "))
annual_income = float(input("Enter your annual income (₹): "))

if mark >= 85:
    if annual_income <= 200000:
        print("Eligible for Scholarship")
    else:
        print("Not Eligible for Scholarship")
else:
    print("Marks not sufficient")
"""
Sample Inputs and Outputs:

Case 1: Eligible
Input:
Enter your marks (%): 90  
Enter your annual income (₹): 180000  
output:
Eligible for Scholarship

Case 2: High marks but high income
Input:
Enter your marks (%): 88  
Enter your annual income (₹): 250000  
output:
Not Eligible for Scholarship

Case 3: Low marks
Input:
Enter your marks (%): 70  
Enter your annual income (₹): 150000  
output:
Marks not sufficient
"""