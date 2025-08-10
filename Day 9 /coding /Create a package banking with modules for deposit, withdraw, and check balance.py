"""Create a package banking with modules for deposit, withdraw, and check balance

Folder Structure:

banking/
    __init__.py
    deposit.py
    withdraw.py
    check_balance.py
main.py
"""

#banking/deposit.py

def deposit(balance, amount):
    return balance + amount

#banking/withdraw.py

def withdraw(balance, amount):
    if amount <= balance:
        return balance - amount
    else:
        print("Insufficient funds")
        return balance

#banking/check_balance.py

def check_balance(balance):
    print("Current Balance:", balance)

#main.py

from banking import deposit, withdraw, check_balance

balance = 1000
balance = deposit.deposit(balance, 500)
check_balance.check_balance(balance)

balance = withdraw.withdraw(balance, 200)
check_balance.check_balance(balance)

#Sample Output:Current Balance: 1500 Current Balance: 1300

