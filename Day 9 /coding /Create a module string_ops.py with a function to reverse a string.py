#Create a module string_ops.py with a function to reverse a string

#File: string_ops.py

def reverse_string(s):
    return s[::-1]

File: main.py

import string_ops

text = "Hello"
print("Original:", text)
print("Reversed:", string_ops.reverse_string(text))

"""Explanation:

s[::-1] reverses a string.

We create string_ops.py as a module and import it into another file.
Output:
Original: Hello
Reversed: olleH
"""