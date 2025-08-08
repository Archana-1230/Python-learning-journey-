Basics of Dictionary

Definition: Collection of key-value pairs, unordered, mutable, and indexed by keys.

Syntax:

my_dict = {"name": "Alice", "age": 25}


2️⃣ Nested Dictionaries

Purpose: Store hierarchical data.

Example:

student_data = {
    "John": {"math": 85, "science": 90},
    "Emma": {"math": 92, "science": 88}
}
print(student_data["Emma"]["science"])  # Output: 88


3️⃣ Dictionary Comprehensions

Create dictionary in one line:

squares = {x: x**2 for x in range(5)}
print(squares)  # {0: 0, 1: 1, 2: 4, 3: 9, 4: 16}


4️⃣ Merging Dictionaries

Using update():

d1 = {"a": 1, "b": 2}
d2 = {"b": 3, "c": 4}
d1.update(d2)
print(d1)  # {'a': 1, 'b': 3, 'c': 4}


5️⃣ Sorting Dictionaries

By key:

data = {"b": 2, "a": 1, "c": 3}
sorted_dict = dict(sorted(data.items()))

By value:

sorted_dict = dict(sorted(data.items(), key=lambda x: x[1]))
