What is a String?

A string in Python is a sequence of Unicode characters enclosed in single ('...') or double ("...") quotes.

Example:
name = "Python"
🔹 Basic String Operations:

s = "Python"
print(len(s))          # 6
print(s[0])            # 'P'
print(s[-1])           # 'n'
print(s[1:4])          # 'yth'


🔹 String Methods (Basic to Intermediate):

s = "  hello PYTHON  "
print(s.strip())        # removes whitespace
print(s.lower())        # 'hello python'
print(s.upper())        # 'HELLO PYTHON'
print(s.title())        # 'Hello Python'
print(s.replace("PYTHON", "World"))  # '  hello World  '
print(s.startswith("  h"))           # True
print(s.endswith("N  "))             # True
print(s.find("PY"))      # 8 (index)


🔹 String Validation Methods:

s = "Python123"
print(s.isalpha())    # False
print(s.isdigit())    # False
print(s.isalnum())    # True
print(s.isspace())    # False


🔹 String Formatting (f-string):

name = "Marry"
age = 21
print(f"My name is {name} and I am {age} years old.")


🔹 Advanced Topics:

🔸 String Join & Split:

words = ['Python', 'is', 'fun']
print(" ".join(words))  # 'Python is fun'

sentence = "Python,is,easy"
print(sentence.split(','))  # ['Python', 'is', 'easy']

🔸 Reversing a String:

s = "Python"
print(s[::-1])  # 'nohtyP'

