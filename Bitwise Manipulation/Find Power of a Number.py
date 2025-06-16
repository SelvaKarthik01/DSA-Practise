# Find the Power of a Number without using any Expoenentiation Function
# This code finds the power of a number using bitwise operations
base = int(input("Enter the base number: "))
p = int(input("Enter the power: "))
ans = 1
while(p != 0):
    if(p & 1):
        ans *= base
    base *= base
    p >>= 1
print(ans)