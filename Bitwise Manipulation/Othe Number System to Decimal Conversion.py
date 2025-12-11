n = int(input("Enter the Number : "))
base = int(input("Enter the Base : "))
ans = 0
temp = base 
base = 1
while(n > 0):
    ans += ((n % temp)*base) 
    base *= temp 
    n = n //10
print(ans)
