L = eval(input("Enter the List : "))
k = int(input("Enter the Sum K : "))
def recursion(L,ans,i,k):
    if i == len(L):
        if sum(ans) == k:
            print(ans)
            return True
        return False
    ans.append(L[i])   # -> Pick the Element 
    if(recursion(L,ans,i+1,k)==False):
        ans.pop()    # -> not Pick the Element 
        if(recursion(L,ans,i+1,k)==False):
            return False
        else:
            return True
    else:
        return True
recursion(L,[],0,k)