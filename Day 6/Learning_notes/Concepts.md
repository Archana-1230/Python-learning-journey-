TUPLE – Immutable List

✅ Concepts & Explanation:

Tuple is a collection which is ordered, immutable, and allows duplicate values.

Tuples are defined using round brackets (), unlike lists which use [].


# Creating a tuple
t = (1, 2, 3)
print(t[0])  # Output: 1

✅ Key Properties:

Immutable: You cannot change the elements once created.

Indexed: You can access elements using index.

Duplicates allowed: (1, 2, 2) is valid.

Can be nested.

Can be used as keys in a dictionary if all elements are immutable.

Faster than lists for read-only operations.


✅ Tuple Methods:

Method	Description

count(x)	Returns the number of times x appears
index(x)	Returns the index of the first occurrence of x


🔹 PART 2: SET – Unordered Unique Items

✅ Concepts & Explanation:

A Set is an unordered, mutable, unindexed collection that stores only unique values.

Duplicates are automatically removed.

Created using {} or set().


s = {1, 2, 2, 3}
print(s)  # Output: {1, 2, 3}

✅ Key Properties:

Unordered: No guarantee of item order.

No duplicates allowed.

Mutable: You can add or remove items.

Useful for set operations like union, intersection, difference.


✅ Set Methods:

Method	Description

add(x)	Adds item x to the set
remove(x)	Removes x; raises error if not found
discard(x)	Removes x if present, no error otherwise
union(set2)	Returns a new set with elements from both
intersection(set2)	Returns common elements
difference(set2)	Elements in set1 but not in set2



🔹 PART 3: DICTIONARY – Key-Value Pair Store

✅ Concepts & Explanation:

Dictionary is a key-value pair collection.

Keys must be unique and immutable (e.g., strings, numbers, tuples).

Values can be any data type.

Allows fast lookups via keys.


d = {'name': 'John', 'age': 25}
print(d['name'])  # Output: John

✅ Key Properties:

Unordered (insertion order preserved from Python 3.7+).

Keys are case-sensitive.

Nested dictionaries allowed.


✅ Dictionary Methods:

Method	Description

get(key)	Returns value if key exists; else None
keys()	Returns all keys
values()	Returns all values
items()	Returns all key-value pairs
pop(key)	Removes key and returns its value
update(dict)	Adds or updates key-value pairs

