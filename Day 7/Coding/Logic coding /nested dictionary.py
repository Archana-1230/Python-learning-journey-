#Create a nested dictionary for 3 students and their subject scores

students = {
    "John": {"Math": 85, "Science": 90},
    "Alice": {"Math": 78, "Science": 88},
    "Bob": {"Math": 92, "Science": 80}
}

print(students)

#Output:{'John': {'Math': 85, 'Science': 90}, 'Alice': {'Math': 78, 'Science': 88}, 'Bob': {'Math': 92, 'Science': 80}}

# Retrieve a specific subject score from the nested dictionary

print("Alice's Science score:", students["Alice"]["Science"])

#Output:Alice's Science score: 88
