s = input("Enter the Number String : ")
d = {2:"abc",3:"def",4:"ghi",5:"jkl",6:"mno",7:"pqrs",8:"tuv",9:"wxyz"}

ans = []
def recursion(s,i,d,ans,ds):
    if i == len(s):
        ans.append("".join(ds))
        return 
    for k in range(len(d[int(s[i])])):
        ds.append(d[int(s[i])][k])
        recursion(s,i+1,d,ans,ds)
        ds.pop()
ans = []
recursion(s,0,d,ans,[])
print(ans)