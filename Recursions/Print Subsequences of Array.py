L = eval(input("Enter the List : "))
ans = []
def recursion(L,i,ans):
    if i == len(L):
        print(ans)
        return 
    ans.append(L[i])   # -> Pick the Element 
    recursion(L,i+1,ans)
    ans.pop()           # -> Not Picking the Element 
    recursion(L,i+1,ans)
recursion(L,0,ans)