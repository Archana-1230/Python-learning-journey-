#Use random to generate 5 random integers between 1 and 100

import random
for _ in range(5):
    print(random.randint(1, 100))

"""Explanation:

randint(a, b) returns a random integer between a and b (inclusive).

Loop runs 5 times to generate 5 numbers.
Sample Output:
73
15
88
4
92"""