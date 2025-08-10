Python Modules & Packages

1. What is a Module?

A module is just a .py file containing Python code — functions, classes, and variables — that you can reuse in other Python files.

💡 Why use modules?

Avoid writing the same code again and again.

Keep projects organized into smaller, logical pieces.

How it Works

1. Python searches for the module in:

The current folder

Installed site-packages

Python's standard library path



2. Once found, it executes the module code once and stores it in memory.


3. You can then use the functions, classes, or variables inside it.



Example

math_utils.py

def add(a, b):
    return a + b

main.py

import math_utils

result = math_utils.add(5, 3)
print(result)  # Output: 8

Explanation:

import math_utils loads and runs math_utils.py.

You access add() by math_utils.add().

2. Types of Modules

a) Built-in Modules

Come with Python installation.
Example: math, os, datetime.

import math
print(math.sqrt(25))  # Output: 5.0

How it works:

Python has a pre-written math module in its standard library.

When you import math, Python loads it from the standard library path.

b) User-defined Modules

You create them yourself.

c) External Modules

Installed via pip (Python package manager).
Example:

pip install requests

import requests
response = requests.get("https://api.github.com")
print(response.status_code)

How it works:

pip downloads the module from PyPI (Python Package Index).

It gets stored in the site-packages folder.

You can then import it like any module.

3. Importing Modules (4 Ways)

1️⃣ Import Entire Module

import math
print(math.pi)

Must use the module name before function.

2️⃣ Import Specific Functions

from math import sqrt
print(sqrt(36))  # No need for math.sqrt

3️⃣ Import with Alias

import math as m
print(m.ceil(4.2))

Alias helps shorten module names.

4️⃣ Import All Functions

from math import *
print(factorial(5))

⚠️ Warning: Not recommended — can cause name conflicts.



4. What is a Package?

A package is a collection of related modules in a folder with an __init__.py file.


Folder Structure

my_package/
    __init__.py
    add.py
    subtract.py

add.py

def add(a, b):
    return a + b

main.py

from my_package import add
print(add.add(10, 5))

How it Works:

__init__.py tells Python that this folder is a package.

The import path tells Python which file to look inside.




5. __name__ == "__main__" Trick

This ensures some code runs only when the file is run directly, not when imported.

file1.py

def greet():
    print("Hello!")

if __name__ == "__main__":
    print("Running directly")

file2.py

import file1

Output:
Running directly  # Only when run directly

6. Real-time Examples

Example 1 – Banking System Modules

banking/
    __init__.py
    auth.py
    transactions.py
    reports.py

auth.py → login, signup functions

transactions.py → deposit, withdraw functions

reports.py → generate monthly statements


This keeps your project organized.

Example 2 – File Organizer

import os, shutil

for file in os.listdir():
    if file.endswith(".txt"):
        shutil.move(file, "TextFiles")

Uses os to list files and shutil to move them.

Example 3 – Data Analysis

import pandas as pd
df = pd.read_csv("sales.csv")
print(df.head())

Uses an external package to read and analyze CSV data.
