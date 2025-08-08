#Merge two dictionaries using both update() and |

dict1 = {"a": 1, "b": 2}
dict2 = {"c": 3, "d": 4}

# Using update()
dict1.update(dict2)
print("Merged using update():", dict1)

# Using | (Python 3.9+)
dict3 = {"x": 10, "y": 20}
dict4 = {"z": 30}
merged_dict = dict3 | dict4
print("Merged using | :", merged_dict)

"""Output:Merged using update(): {'a': 1, 'b': 2, 'c': 3, 'd': 4}
Merged using | : {'x': 10, 'y': 20, 'z': 30}"""

