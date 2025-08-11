#Calculate Average Marks from CSV

#Explanation:We use the csv module to read structured data. We sum the marks and divide by the number of students to find the average.

import csv

total = 0
count = 0

with open("students.csv", "r") as f:
    reader = csv.reader(f)
    next(reader)  # Skip header row
    for row in reader:
        total += int(row[1])  # Assuming marks are in 2nd column
        count += 1

average = total / count
print(f"Average Marks: {average}")
