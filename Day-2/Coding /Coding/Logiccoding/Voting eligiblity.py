"""
Input:
Enter the age: 20
output:
Eligible to vote
"""
# Check if a person is eligible to vote
age = int(input("Enter the age: "))
if age >= 18:
    print("Eligible to vote")
else:
    print("Not eligible to vote")