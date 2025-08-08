Advanced Dictionary in Python
Q1: Which is the correct way to create a dictionary?
A) dict = (key1: value1, key2: value2)
B) dict = {key1: value1, key2: value2}
C) dict = [key1: value1, key2: value2]
D) dict(key1: value1, key2: value2)
✅ Answer: B


Q2: How do you access "science" score for "Emma" in a nested dictionary student_data?
A) student_data["Emma"].science
B) student_data["Emma"]["science"]
C) student_data["science"]["Emma"]
D) student_data["Emma"][science]
✅ Answer: B


Q3: What will be the output of:

d = {"a": 1, "b": 2}
d["c"] = 3
print(d)

A) {"a": 1, "b": 2, "c": 3}
B) {"a": 1, "b": 2}
C) Error
D) {"c": 3}
✅ Answer: A


Q4: Which operator is used to merge dictionaries in Python 3.9+?
A) &
B) |
C) +
D) ||
✅ Answer: B


Q5: What does the following code print?

d1 = {"a": 1, "b": 2}
d2 = {"b": 3, "c": 4}
print(d1 | d2)

A) {'a': 1, 'b': 2, 'c': 4}
B) {'a': 1, 'b': 3, 'c': 4}
C) Error
D) {'b': 3, 'c': 4}
✅ Answer: B


Q6: What is the output?

data = {"x": 10, "y": 5, "z": 15}
print(sorted(data))

A) ['x', 'y', 'z']
B) [10, 5, 15]
C) [('x', 10), ('y', 5), ('z', 15)]
D) Error
✅ Answer: A


Q7: Which method removes all items from a dictionary?
A) clear()
B) pop()
C) del()
D) remove()
✅ Answer: A


Q8: Which of the following is not allowed in Python dictionaries?
A) String as key
B) Tuple as key
C) List as key
D) Integer as key
✅ Answer: C


Q9: How can you iterate over both keys and values in a dictionary?
A) for key, value in dict:
B) for key, value in dict.items():
C) for key, value in dict.values():
D) for key, value in dict.keys():
✅ Answer: B

Q10: What is the output of:

data = {n: n**2 for n in range(3)}
print(data)

A) {0: 0, 1: 1, 2: 4}
B) [0, 1, 4]
C) [(0, 0), (1, 1), (2, 4)]
D) Error
✅ Answer: A