Decision Making + Loops + Patterns

1.Conditional Statements in Python

if condition:
    # do something
elif another_condition:
    # do something else
else:
    # fallback

2.Nested if-else

if condition1:
    if condition2:
        # Both true
    else:
        # Only condition1 true
else:
    # condition1 false
Example:
1. Basic if
age = 18
if age >= 18:
    print("Eligible to vote")

2. if-else
num = 5
if num % 2 == 0:
    print("Even")
else:
    print("Odd")

3. if-elif-else
marks = 75
if marks >= 90:
    print("Grade A")
elif marks >= 75:
    print("Grade B")
else:
    print("Grade C")

4. Nested if
x = 10
if x > 5:
    if x < 20:
        print("Between 5 and 20")


3.Loops Overview

Loop Type	Syntax

for	->for i in range(n):
while->while condition:
Loop control:
break, continue,pass
else with loops

*break statement:
The break statement terminates the current loop entirely and transfers control to the statement immediately following the loop. It is used to exit a loop prematurely based on a specific condition. 
for i in range(5):
    if i == 3:
        break  # Exit the loop when i is 3
    print(i)
# Output:
# 0
# 1
# 2

*continue statement:
The continue statement skips the rest of the code within the current iteration of a loop and proceeds to the next iteration. It does not terminate the loop entirely but moves to the next cycle. [1]  
for i in range(5):
    if i == 2:
        continue  # Skip printing when i is 2
    print(i)
# Output:
# 0
# 1
# 3
# 4

*pass statement :        
The pass statement is a null operation; it does nothing. It is used as a placeholder when a statement is syntactically required but no action needs to be performed. This is often used in preliminary code structures or empty blocks that will be filled in later. 
def my_function():
    pass  # Placeholder for future implementation

if True:
    pass  # Placeholder for a conditional block
else:
    print("This will not be printed.")

for i in range(3):
    if i == 1:
        pass  # Do nothing when i is 1
    else:
        print(i)
# Output:
# 0
# 2
example:
for loop:
for i in range(5):
    print(i)

🔄 while loop:

i = 0
while i < 5:
    print(i)
    i += 1

🛑 break and continue:

for i in range(5):
    if i == 3:
        break
    print(i)

for i in range(5):
    if i == 3:
        continue
    print(i)

🔁 else with loops:

for i in range(3):
    print(i)
else:
    print("Loop done")


