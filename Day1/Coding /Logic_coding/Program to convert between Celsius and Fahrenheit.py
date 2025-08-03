#program to convert temperatures
Choice=input("Enter your choice (c/f): "). upper()
if Choice=='C':
    c=float(input("Enter the Celsius:"))
    F=(c*9/5)+32
    print(f"Convert  to Fahrenheit: {F:.2f}°F")
elif Choice=='F':
    F=float(input("Enter the Fahrenheit:"))
    C=(F-32)*5/9
    print(f"Convert to Celsius: {C:.2f}°C")
else:
    print("Invalid ")
"""
Input1:
Enter your choice (C/F): C
Enter the Celsius: 37
output1:
Convert to Fahrenheit: 98.60°F

Input2:
Enter your choice (C/F): f
Enter the Fahrenheit: 98.6
output2:
Convert to Celsius: 37.00°C
"""