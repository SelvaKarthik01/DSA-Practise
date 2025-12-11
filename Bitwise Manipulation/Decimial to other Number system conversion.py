n = int(input("Enter the Decimal Number : "))
base = int(input("Enter the Base of the Number : "))
ans = 0 
count = 0
while(n > 0):
    rem = n % base 
    ans += (rem*(10**count)) 
    count += 1
    n = n //base 
print(ans)