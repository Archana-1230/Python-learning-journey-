# Calculate the area and perimeter of a rectangle.
# Formula:
# area -> length * breadth 
# perimeter -> 2 * (length + breadth)

Length = int(input("Enter the length: "))
breadth = int(input("Enter the breadth: "))

# Calculating area and perimeter
area = Length * breadth
perimeter = 2 * (Length + breadth)

# Displaying results
print("Area of rectangle:", area)
print("Perimeter of rectangle:", perimeter)
"""input:
Enter the length: 10
Enter the breadth: 5
output:
Area of rectangle: 50
Perimeter of rectangle: 30
"""