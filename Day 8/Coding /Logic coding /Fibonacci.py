"""Recursive Fibonacci

Explanation:
Fibonacci sequence: F(n) = F(n-1) + F(n-2).
"""
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n-1) + fibonacci(n-2)

print([fibonacci(i) for i in range(6)]) 
#Sample Output:[0, 1, 1, 2, 3, 5]
