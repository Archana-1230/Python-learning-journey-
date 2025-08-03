#Reverse the digit
a=int(input("Enter the digit:"))
c=0
while a>0:
    d=a%10
    c=c*10+d
    a//=10
print(c)
"""
Input:
Enter the digit: 1234
output:
4321
"""
