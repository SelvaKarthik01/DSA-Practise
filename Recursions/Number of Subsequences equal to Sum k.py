L = eval(input("Enter the Number : "))
k = int(input("Enter the Sum K : "))
def recursion(L,i,k,ans):
    if i == len(L):
        if sum(ans) == k:
            return 1 
        else:
            return 0
    ans.append(L[i])
    l = recursion(L,i+1,k,ans)
    ans .pop()
    r = recursion(L,i+1,k,ans)
    return l + r
print(recursion(L,0,k,[]))