nums = eval(input("Enter the List : "))
d = {}
for i in range(len(nums)):
    d[nums[i]] = i 
    ans = 1
    for i in d:
        if i-1 not in d:
            count = 0 
            temp = i
            while(True):
                if temp not in d:
                    break
                count += 1
                temp += 1
            ans = max(count,ans)
print(ans)