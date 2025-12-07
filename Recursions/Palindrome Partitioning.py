s = input("Enter the String : ")

def isPalindrome(s):
    if s==s[::-1]:
        return True 
    else:
        return False

def recursion(s,i,path,ans):
    if i == len(s):
        ans.append(list(path))
        return 
    for k in range(i,len(s)):
        if isPalindrome(s[i:k+1]):
            path.append(s[i:k+1])
            recursion(s,k+1,path,ans)
            path.pop()
ans = []
recursion(s,0,[],ans)
print(ans)