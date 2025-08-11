#Merge Two Text Files into One

#Explanation:We read both files and write their contents into a new file using "w" mode. This is useful for combining reports or data.

# Merge part1.txt and part2.txt into full_report.txt
with open("part1.txt", "r") as f1, open("part2.txt", "r") as f2:
    data1 = f1.read()
    data2 = f2.read()

with open("full_report.txt", "w") as f3:
    f3.write(data1 + "\n" + data2)

print("Files merged successfully.")
