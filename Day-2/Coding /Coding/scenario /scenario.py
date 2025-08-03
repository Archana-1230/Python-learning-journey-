"""Scenario: Billing with Discount
Take user name, bill amount
If bill > 1000, give 10% discount
Print final amount"""
name = input("Enter customer name: ")
bill = float(input("Enter bill amount: "))
if bill > 1000:
    bill *= 0.9  # Apply 10% discount
print("Hi", name + ", your final bill is:", bill)
