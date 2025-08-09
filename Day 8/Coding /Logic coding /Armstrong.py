"""
An Armstrong number (also called narcissistic number) is a number that is equal to the sum of its own digits each raised to the power of the number of digits.

For example:

153 → 3 digits →  ✅ Armstrong

9474 → 4 digits →  ✅ Armstrong

123 →  ❌ Not Armstrong
"""
#coding
def is_armstrong(num):
    digits = [int(d) for d in str(num)]
    power = len(digits)
    return sum(d**power for d in digits) == num
    
"""
Sample Input & Output

Input:

153
9474
123

Output:

True
True
False

"""