Q1. What is the default mode of open()?

a) w

✅ b) r

c) a

d) rb


Explanation:
By default, open() opens files in read mode ("r"). If the file does not exist, it raises an error in this mode.



Q2. Which method reads an entire file into a list of lines?

a) read()

b) readline()

✅ c) readlines()

d) readall()


Explanation:
readlines() returns a list, where each element is a line from the file, including \n characters.


Q3. What happens if "w" mode is used on an existing file?

a) Appends data

b) Deletes the file

✅ c) Overwrites the file

d) Throws an error


Explanation:
"w" mode creates a new empty file if it doesn’t exist, or overwrites existing content if it does.

Q4. Which keyword is best for automatic file closing?

a) close

b) close()

✅ c) with

d) exit


Explanation:
The with statement is used for context management and ensures files are closed automatically, even if an error occurs.

Q5. What will this code do?

open("test.txt", "x")

✅ a) Creates a new file

b) Opens existing file

c) Deletes file

d) Reads file


Explanation:
"x" mode creates a new file but raises an error if the file already exists.


Q6. How do you read a binary file?

✅ a) "rb"

b) "br"

c) "wb"

d) "bw"


Explanation:
"rb" stands for read binary mode, used for non-text files like images, audio, or executables.



Q7. Which library is used to work with CSV files?

✅ a) csv

b) json

c) pandas

d) excel


Explanation:
Python’s built-in csv module helps read and write Comma-Separated Values (CSV) files.


Q8. What is f.seek(0) used for?

a) Closes file

✅ b) Resets pointer to start

c) Deletes file

d) Reads file


Explanation:
seek(0) moves the file pointer to the beginning of the file so reading can start again.


Q9. Which module handles JSON in Python?

a) csv

✅ b) json

c) data

d) dict


Explanation:
The json module allows encoding Python objects into JSON format and decoding JSON into Python objects.



Q10. What happens if you try to open a non-existing file in "r" mode?

a) Creates file

b) Appends

✅ c) Error

d) Overwrites


Explanation:
"r" mode requires the file to exist. If it doesn’t, Python raises a FileNotFoundError.