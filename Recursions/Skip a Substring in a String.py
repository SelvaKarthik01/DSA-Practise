# To Skip a Substring in a String using recurisons


def skip_substring(s,ans,sub,index):
    if index == len(s):
        return ans
    if s[index] == "a" and s[index:len(sub)+index] == sub:
        return skip_substring(s,ans,sub,index+len(sub))
    ans += s[index]
    return skip_substring(s,ans,sub,index+1)

s = input("Enter the String : ")
sub = input("Enter the Substring : ")
print(skip_substring(s,"",sub,0))    