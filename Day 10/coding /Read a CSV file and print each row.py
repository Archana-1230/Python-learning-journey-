#Read a CSV file and print each row.
#Concepts: csv module, reading structured data.

import csv

with open("students.csv", "r") as f:
    reader = csv.reader(f)
    for row in reader:
        print(row)
