#Employee Directory

employees = {
    101: {"name": "John", "role": "Manager", "salary": 60000},
    102: {"name": "Alice", "role": "Developer", "salary": 50000},
}

# Add a new employee
employees[103] = {"name": "Bob", "role": "Designer", "salary": 45000}

# Update salary of Alice
employees[102]["salary"] = 55000

print(employees)

#Output:{101: {'name': 'John', 'role': 'Manager', 'salary': 60000}, 102: {'name': 'Alice', 'role': 'Developer', 'salary': 55000}, 103: {'name': 'Bob', 'role': 'Designer', 'salary': 45000}}

