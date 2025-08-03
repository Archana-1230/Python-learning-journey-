"""Input: n = 15
Output: odd
Explanation: The number is not divisible by 2, Odd number."""
"""Input: n = 44
Output: True
Explanation: The number is divisible by 2, Even number.
"""
n=int(input("Enter number:"))
if n%2==0:
    print("Even Number")
else:
    print("odd Number")