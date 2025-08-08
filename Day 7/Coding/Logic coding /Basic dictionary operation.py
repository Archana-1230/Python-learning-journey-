# -------------------------------
# BASIC DICTIONARY OPERATIONS
# -------------------------------

# 1. Create a dictionary with 5 key-value pairs and print it
fruits = {
    "Apple": 120,
    "Banana": 40,
    "Cherry": 250,
    "Orange": 80,
    "Grapes": 90
}
print("Initial Dictionary:", fruits)
#output:{'Apple': 120, 'Banana': 40, 'Cherry': 250, 'Orange': 80, 'Grapes': 90}

# 2. Access a specific value using a key
print("Price of Apple:", fruits["Apple"])
#output:Price of Apple: 120

# 3. Add a new key-value pair
fruits["Pineapple"] = 150
print("After adding Pineapple:", fruits)
#output:{'Apple': 120, 'Banana': 40, 'Cherry': 250, 'Orange': 80, 'Grapes': 90, 'Pineapple': 150}

# 4. Delete a key from the dictionary
del fruits["Banana"]
print("After deleting Banana:", fruits)
#output:{'Apple': 120, 'Cherry': 250, 'Orange': 80, 'Grapes': 90, 'Pineapple': 150}

# 5. Check if a key exists
if "Apple" in fruits:
    print("Apple is available.")
else:
    print("Apple is not available.")
#output:Apple is available.