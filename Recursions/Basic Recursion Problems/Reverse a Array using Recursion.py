L = eval(input("Enter the Number N : "))
"""def recursion(L,l,r):  # Two Pointer Approach 
    if l >= r:
        return L
    L[l],L[r] = L[r],L[l]
    return recursion(L,l+1,r-1)    
print(recursion(L,0,len(L)-1))"""

def recursion1(L,i):
    if i >= len(L)//2:
        return L
    L[i],L[len(L)-1-i]=L[len(L)-i-1],L[i]
    return recursion1(L,i+1)
print(recursion1(L,0))