L = eval(input("Enter the List : "))
ans = []
for i in range(len(L)):
    subarray = list()
    subarray.append(L[i])
    ans.append(subarray[:])
    for j in range(i+1,len(L)):
        subarray.append(L[j])
        ans.append(subarray[:])
print(ans)