#Count the number of words in a file.
#Concepts: split(), text processing.

# Count words in a file
with open("my_name.txt", "r") as f:
    content = f.read()

word_count = len(content.split())
print(f"Total words: {word_count}")
