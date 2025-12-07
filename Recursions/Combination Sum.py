L = eval(input("Enter the List : "))
k = int(input("Enter the Sum : "))
def recursion(L,i,sum,ds,ans):
    if i == len(L) :
        if sum==0:
            ans.append(list(ds))
        return
    if L[i] <= sum:
        ds.append(L[i])
        recursion(L,i,sum-L[i],ds,ans)
        ds.pop()
    recursion(L,i+1,sum,ds,ans)
ans = []
recursion(L,0,k,[],ans)
print(ans)
        