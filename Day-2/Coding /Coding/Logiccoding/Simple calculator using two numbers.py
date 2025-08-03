"""
input:
Enter Value1: 12  
Enter Value2: 4  
Enter the Operator (+, -, *, /, //, %): *
output:
Result: 48
"""
# Simple calculator using two numbers
a = int(input("Enter Value1: "))
b = int(input("Enter Value2: "))
operator = input("Enter the Operator (+, -, *, /, //, %): ")

if operator == '+':
    print("Result:", a + b)
elif operator == '-':
    print("Result:", a - b)
elif operator == '*':
    print("Result:", a * b)
elif operator == '/':
    if b != 0:
        print("Result:", a / b)
    else:
        print("Error: Division by zero")
elif operator == '//':
    if b != 0:
        print("Result:", a // b)
    else:
        print("Error: Division by zero")
elif operator == '%':
    if b != 0:
        print("Result:", a % b)
    else:
        print("Error: Division by zero")
else:
    print("Invalid operator")
  