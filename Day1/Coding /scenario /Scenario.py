"""Scenario:
A billing system asks the user for:
Customer name
2 item prices
Display total with greeting
"""
name=input("Enter your name: ")
item1=float(input("Enter price of item 1: "))
item2=float(input("Enter price of item 2: "))
total=item1 + item2
print("Hi", name + ", your total bill is:", total)


