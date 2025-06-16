#To Find the Square Root fo a Number using Divide and Conquer Approach 
import math
n = int(input("Enter the Number N "))
L = list(range(1,n+1))
s = 0 
end = len(L)-1
while(s <= end):
    mid = (s + end) //2
    if (mid * mid > n):
        end = mid - 1
    if mid * mid == n:
        print(mid)
        break
    if (mid * mid < n):
        s = mid + 1
else:
    root = mid -1
    # Newton Raphsons Formula for Finding the Precise Square Root
    print((root+n/root)/2)
    # This root value is jutrs va repcise estimate of the value
    
