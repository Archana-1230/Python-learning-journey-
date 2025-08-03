"""
input:
Enter the value: 15
output:
Divisible by 3 & 5
"""
# Check if a number is divisible by 3, 5, or both
a = int(input("Enter the value: "))
if a % 3 == 0 and a % 5 == 0:
    print("Divisible by 3 & 5")
elif a % 3 == 0:
    print("Divisible by 3")
elif a % 5 == 0:
    print("Divisible by 5")
else:
    print("Not divisible by 3 and 5")