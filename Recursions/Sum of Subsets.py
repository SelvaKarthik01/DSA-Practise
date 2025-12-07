L = eval(input("Enter the List : "))
ans = []
L.sort()
def recursion(L,i,sum,ans):
    if i == len(L):
        ans.append(sum)
        return 
    recursion(L,i+1,sum+L[i],ans)
    recursion(L,i+1,sum,ans)
recursion(L,0,0,ans)
ans.sort()
print(ans)