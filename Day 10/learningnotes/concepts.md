Basic File Operations

In Python, file handling uses the built-in open() function:

open(file, mode)

Common Modes:

"r" → Read (default)

"w" → Write (overwrites existing file)

"a" → Append

"b" → Binary mode

"x" → Create new file (error if exists)

Add + for read/write ("r+", "w+")


# Example: Writing to a file
with open("notes.txt", "w") as f:
    f.write("Hello, Python!\n")

✅ Using with automatically closes the file.

Reading Files

with open("notes.txt", "r") as f:
    content = f.read()
print(content)

Other methods:

read() → entire file

readline() → one line

readlines() → list of all lines


Writing & Appending

# Append a line
with open("notes.txt", "a") as f:
    f.write("New line added!\n")

File Pointer & Tell

f.seek(position)  # move pointer
f.tell()          # get current position

Binary File Handling

# Write binary data
with open("image.jpg", "rb") as f:
    data = f.read()


Advanced Concepts

Exception Handling in File I/O

CSV & JSON file handling (csv, json modules)

File existence check using os.path.exists()

Working with paths using pathlib
