#Attendance Check

registered = {"A", "B", "C", "D"}
present = {"A", "C"}
absent = registered - present
print(f"Absent students: {absent}")
"""
🔍 Explanation:

- is the difference operator.

It returns students who are registered but not present.

Output:
Absent students: {'B', 'D'}"""