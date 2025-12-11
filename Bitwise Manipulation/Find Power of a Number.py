# Find the Power of a Number without using any Expoenentiation Function
# This code finds the power of a number using bitwise operations
base = int(input("Enter the Number : "))
p = int(input("Enter the Power : "))
ans = 1
while(p > 0):
    if p & 1:
        ans *= base 
    base *= base 
    p = p >> 1
print(ans)