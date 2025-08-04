# Login System (username: admin, password: 1234)
username = input("Enter the username: ")
password = input("Enter the password: ")

if username == 'admin' and password == "1234":
    print("Login successfully")
else:
    print("Invalid Credential")
"""
Sample Input and Output:
Case 1: Correct Credentials
Input:
Enter the username: admin
Enter the password: 1234
output:
Login successfully

Case 2: Incorrect Username
Input:
Enter the username: user
Enter the password: 1234
output:
Invalid Credential
"""