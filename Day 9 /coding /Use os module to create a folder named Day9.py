#Use os module to create a folder named Day9

import os

folder_name = "Day9"
if not os.path.exists(folder_name):
    os.mkdir(folder_name)
    print(f"Folder '{folder_name}' created.")
else:
    print(f"Folder '{folder_name}' already exists.")

"""Explanation:

os.mkdir() creates a folder.

os.path.exists() checks if the folder already exists.


Output:
Folder 'Day9' created.

(or)

Folder 'Day9' already exists."""