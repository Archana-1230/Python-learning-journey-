"""A Perfect Number is a positive integer that is equal to the sum of its proper divisors (excluding itself).

Examples:

6 → Divisors: 1, 2, 3 → Sum = 1 + 2 + 3 = 6 ✅ Perfect

28 → Divisors: 1, 2, 4, 7, 14 → Sum = 1 + 2 + 4 + 7 + 14 = 28 ✅ Perfect

12 → Divisors: 1, 2, 3, 4, 6 → Sum = 16 ❌ Not Perfect

"""

#Code Implementation

def is_perfect(num):
    if num < 2:
        return False
    
    divisors_sum = 1  # 1 is always a divisor
    for i in range(2, num // 2 + 1):
        if num % i == 0:
            divisors_sum += i
    
    return divisors_sum == num

print(is_perfect(num))


"""Sample Input & Output

Input:
6
28
12

Output:
True
True
False
"""
