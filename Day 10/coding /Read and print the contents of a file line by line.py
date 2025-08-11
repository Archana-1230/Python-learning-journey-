#Read and print the contents of a file line by line.
#Concepts: readline(), for loop over file object.

# Read file line by line
with open("my_name.txt", "r") as f:
    for line in f:
        print(line.strip())  # .strip() removes newline
