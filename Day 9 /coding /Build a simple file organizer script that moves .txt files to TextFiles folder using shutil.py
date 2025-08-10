"""Build a simple file organizer script that moves .txt files to TextFiles folder using shutil"""

import os
import shutil

source_folder = "."          # current directory
destination_folder = "TextFiles"

# Create destination folder if it doesn't exist
if not os.path.exists(destination_folder):
    os.mkdir(destination_folder)

# Move all .txt files
for file in os.listdir(source_folder):
    if file.endswith(".txt"):
        shutil.move(file, os.path.join(destination_folder, file))
        print(f"Moved: {file}")

print("File organization complete.")

"""Explanation:

os.listdir() lists all files in the folder.

file.endswith(".txt") filters .txt files.

shutil.move() moves files to the new folder."""


"""Sample Output:

Moved: notes.txt
Moved: todo.txt
File organization complete."""
