import string

password = input("Enter password: ")

special_characters = string.punctuation  # like @, #, $, %, etc.

if len(password) >= 8:
    if any(char.isdigit() for char in password):
        if any(char in special_characters for char in password):
            print("Valid password")
        else:
            print("Password must contain at least one special character")
    else:
        print("Password must contain at least one digit")
else:
    print("Password must be at least 8 characters long")
"""
Sample Input-Output with Explanation:

🔸 Case 1: Valid Password

Enter password: Hello@123

✅ Checks:

Length = 9 → ✅ len(password) >= 8

Contains digits → ✅ 1, 2, 3

Contains special characters → ✅ @


✅ Output:

Valid password

🔸 Case 2: No Digit

Enter password: Hello@abc

✅ Checks:

Length = 9 → ✅

Digits? → ❌ (no digit found)

Special character? → ✅ @


❌ Output:

Password must contain at least one digit


🔸 Case 3: No Special Character

Enter password: Hello1234

✅ Checks:

Length = 9 → ✅

Digit? → ✅ 1, 2, 3, 4

Special character? → ❌ (none)


❌ Output:

Password must contain at least one special character


🔸 Case 4: Short Password

Enter password: H@12

✅ Checks:

Length = 4 → ❌ (too short)


❌ Output:

Password must be at least 8 characters long


🔸 Case 5: Only special character and digit, no letters

Enter password: @1234567

✅ Checks:

Length = 8 → ✅

Digit? → ✅

Special character? → ✅ @


✅ Output:

Valid password
"""