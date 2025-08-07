"""Tuple: Swap Elements

🔍 Swap the first and last elements of a tuple.

Sample Input:

(1, 2, 3, 4)

Sample Output:

(4, 2, 3, 1)
"""
#Code:

t = (1, 2, 3, 4)
t = (t[-1],) + t[1:-1] + (t[0],)
print(t)
