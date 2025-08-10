#Use sys.argv to take a number from the command line and print its square

#File: square.py

import sys

if len(sys.argv) != 2:
    print("Usage: python square.py <number>")
else:
    num = int(sys.argv[1])
    print(f"Square of {num} is {num ** 2}")

"""Run in Terminal:

python square.py 5

Output:

Square of 5 is 25
"""