n1 = int(input("Enter the First number : "))
n2 = int(input("Enter the Second Number : "))
import math
ans = 1
for i in range(1,int(math.sqrt(min(n1,n2))+1)):
    if n1 %i == n2 %i == 0:
        ans = max(ans,i)
print(ans)