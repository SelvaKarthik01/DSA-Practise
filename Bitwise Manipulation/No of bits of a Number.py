# To find the No0 of Bits of a Number using 2 solutions
n1 = int(input("Enter the Number : "))
n = n1
count = 0 
while(n != 0 ):
    count += 1
    n >>=1
print(count)

# Using the log2 function
import math
ans = math.floor(math.log(n1,2))+1
print(ans)

