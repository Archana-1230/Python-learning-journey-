"""Dictionary: Count Characters

 Count occurrences of each character in a string using dictionary.

Sample Input:

apple

Sample Output:

{'a': 1, 'p': 2, 'l': 1, 'e': 1}
"""
#Code:

s = "apple"
d = {}
for char in s:
    d[char] = d.get(char, 0) + 1
print(d)
