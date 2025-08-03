"""
input:
Enter the number of units consumed: 120
output:
Total Electricity Bill: ₹ 600
"""
# Electricity Bill Generator
units = int(input("Enter the number of units consumed: "))
if units < 100:
    bill = units * 2
else:
    bill = units * 5
print("Total Electricity Bill: ₹", bill)