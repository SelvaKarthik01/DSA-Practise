# Find the magic number using bitwise operation
# 5 = 1 0 1 = 1*5^1 + 0*5^2 + 1*5^3 = 130
n = int(input("Enter the Number n : "))
base = 5
temp = base 
ans = 0
while(n > 0):
    if n & 1:
        ans += base 
    base *= temp
    n = n >> 1
print(ans)
    
    