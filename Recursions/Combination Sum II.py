L = eval(input("Enter the List : "))
L.sort()
k = int(input("Enter the Sum K : "))
def recursion(L,i,target,ds,ans):
    if target == 0:
        ans.append(list(ds))
        return 
    for k in range(i,len(L)):
        if k > i and L[k] == L[k-1]:
            continue
        if target < L[k]:
            break 
        ds.append(L[k])
        recursion(L,k+1,target-L[k],ds,ans)
        ds.pop()
ans = []
recursion(L,0,k,[],ans)
print(ans)
        