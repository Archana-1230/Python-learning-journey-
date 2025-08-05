correct_pin = "1234"
attempts = 0
while attempts < 3:
    entered_pin = input("Enter PIN: ")
    if entered_pin == correct_pin:
        print("Access Granted")
        break
    else:
        print("Wrong PIN")
        attempts += 1
else:
    print("Card Blocked")
"""
sample input and output:
Enter PIN: 1111  
Wrong PIN  
Enter PIN: 1234  
Access Granted

"""