L = eval(input("Enter the List : "))
k = int(input("Enter the Number of times elements are repeated : "))
import math
# This is a Array which has all element are repeated k times except one element which is present only one time we need to find that element 
max_bits = int(math.log(max(L),2)+1)

ans = [0]*max_bits
mask = 1
for i in L:
    mask = 1
    while(mask != (1 << (max_bits))):
        if i & mask:
            ans[max_bits-1-(int(math.log(mask,2)))] += 1
        mask = mask << 1
sum = 0
print(ans)
for i in range(len(ans)-1,-1,-1):
    sum += (ans[i]%k)*(2**(len(ans)-1-i))
print(sum)
    
    