dividend = int(input("Enter the Dividend of the Number : "))
divisor = int(input("Enter the Divisor : "))
if dividend == divisor:
    print(1)
if dividend >= 0 and divisor < 0:
    sign = False 
elif dividend < 0 and divisor >= 0:
    sign = False 
else:
    sign = True 
n = abs(dividend)
d = abs(divisor)
ans = 0
while(n>=d):
    
    count = 0 
    while(n >= (d<<(count+1))):
        count += 1
    ans += (1<<count)
    n = n - (d<<count)
if n == 2^31 and sign==True:
    print(float("inf"))
elif n == 2^31 and sign == False:
    print(float("-inf"))
elif sign :
    print(ans)
else:
    print(-1*(ans))
