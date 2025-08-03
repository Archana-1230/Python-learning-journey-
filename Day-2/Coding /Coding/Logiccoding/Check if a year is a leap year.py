# Check if a year is a leap year
year = int(input("Enter the year: "))
# Leap year condition:
# - Divisible by 4 and not divisible by 100
# - OR divisible by 400
if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
    print("It is a leap year")
else:
    print("It is not a leap year")
"""
Input 1:
Enter the year: 2024
Output 1:
It is a leap year

Input 2:
Enter the year: 1900
Output 2:
It is not a leap year
"""