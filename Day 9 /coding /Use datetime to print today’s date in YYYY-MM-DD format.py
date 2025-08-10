#Use datetime to print today’s date in YYYY-MM-DD format

from datetime import date

today = date.today()
print("Today's date:", today.strftime("%Y-%m-%d"))

"""Explanation:

date.today() gives the current date.

strftime("%Y-%m-%d") formats it as YYYY-MM-DD.

Output:

Today's date: 2025-08-10
"""