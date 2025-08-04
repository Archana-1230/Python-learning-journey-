"""Case:
You are designing an ATM withdrawal system.
Requirements:

If balance is sufficient, and withdrawal amount is less than ₹10,000, allow.

If above ₹10,000, show warning message.

If balance insufficient, deny.
"""
balance = int(input())
withdraw = int(input("Enter amount: "))

if withdraw <= balance:
    if withdraw <= 10000:
        print("Withdraw Successful")
    else:
        print("Amount exceeds single transaction limit")
else:
    print("Insufficient Balance")
