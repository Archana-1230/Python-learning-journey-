#Check whether a character is uppercase, lowercase, or a digit.
a = input("Enter a character: ")
if a.isupper():
    print("upper")
elif a.islower():
    print("lower")
elif a.isdigit():
    print("digit")
else:
    print("special character or invalid input")
"""
Sample Input & Output:

Input:

Enter a character: G

Output:

upper

Input:

Enter a character: p

Output:

lower

Input:

Enter a character: 8

Output:

digit

Input:

Enter a character: @

Output:

special character or invalid input
"""