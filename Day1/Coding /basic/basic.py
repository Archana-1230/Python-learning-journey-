#Take your name and age, and greet the user.
name=input("Enter your name:")
age=int(input("Enter your age:"))
print("Hello My name is "+name,"I am",age,"years old")
#Add two numbers input by the user.
a=int(input("Enter first number:"))
b=int(input("Enter second number:"))
print("sum is",a+b)
#Swap two numbers (without using third variable)
a=int(input("Enter first number:"))
b=int(input("Enter second number:"))
print("Before Swapping",a,b)
a,b=b,a
print("After swapping",a,b)
# Convert input to int and float and Check the data type of input.
a=int(input("Enter a:"))
b=float(a)
c=str(a)
print(type(a))
print(type(b))
print(type(c))