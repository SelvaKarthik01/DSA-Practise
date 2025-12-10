L = eval(input("Enter the List : "))
import math
max_count = 1 << len(L)

ans = []
for i in range(max_count):
    mask = 1
    temp = []
    while(mask != (1<<len(L))):
        if i & mask:
            temp.append(L[int(math.log(mask,2))])
        mask = mask << 1
    ans.append(temp)
print(ans)
        
    