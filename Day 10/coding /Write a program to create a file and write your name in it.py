#Write a program to create a file and write your name in it.
#Concepts: open(), write mode, file closing.

# Create a file and write name
with open("my_name.txt", "w") as f:
    f.write("Archana Devi")

print("Name written successfully!")

