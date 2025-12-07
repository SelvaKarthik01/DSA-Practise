k = int(input("Enter the Sum : "))

def recursion(k,ds,ans):
    if k == 0:
        ans.append(list(ds))
        return 
    for i in range(1,7):
        if k - i >= 0:
            ds.append(i)
            recursion(k-i,ds,ans)
            ds.pop()
ans = []
recursion(k,[],ans)
print(ans)