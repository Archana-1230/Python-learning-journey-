#check eligibility for loan
#condition:age>21 and salary>25000
age = int(input())
salary = float(input())

if age >= 21:
    if salary >= 25000:
        print("Eligible for loan")
    else:
        print("Not Eligible for loan")
else:
    print("Age not satisfied")
"""
Sample Inputs and Outputs:
Case 1: Eligible
Input:
25
30000
Output:
Eligible for loan
Case 2: Age OK but salary low
Input:
23
20000
Output:
Not Eligible for loan

Case 3: Age not satisfied
Input:
18
50000
Output:
Age not satisfied
"""