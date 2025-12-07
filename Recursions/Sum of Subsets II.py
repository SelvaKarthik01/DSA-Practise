L = eval(input("Enter the List : "))

def recursion(L,i,ds,ans):
    ans.append(list(ds))
    for k in range(i,len(L)):
        if k != i and L[k] == L[k-1]:
            continue 
        else:
            ds.append(L[k])
            recursion(L,k+1,ds,ans)
            ds.pop()
ans = []
recursion(L,0,[],ans)
print(ans)