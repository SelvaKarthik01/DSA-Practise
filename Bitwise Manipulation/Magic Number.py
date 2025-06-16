# Find the magic number using bitwise operation
# 5 = 1 0 1 = 1*5^1 + 0*5^2 + 1*5^3 = 130
n = int(input("Enter the Number : "))
ans = 0
base = 5
while(n != 0):
    lsb = n & 1
    if lsb == 1:
        ans += base
    base *= 5
    n >>= 1
print(ans)
    
    