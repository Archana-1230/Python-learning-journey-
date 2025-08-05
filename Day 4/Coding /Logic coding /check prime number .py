num = int(input())
is_prime = True
for i in range(2, int(num/2)+1):
    if num % i == 0:
        is_prime = False
        break
print("Prime" if is_prime else "Not Prime")
"""
input:
n=7
output:
Prime
"""
