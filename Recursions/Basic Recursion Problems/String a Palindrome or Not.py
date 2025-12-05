s = input("Enter the String : ")
def recursion(s,i):
    if i >= len(s)//2:   # Using just one Pointer annd using the Same for the last element and iterate the Pointer each by one element
        return True
    if s[i] == s[len(s)-i-1]:
        return recursion(s,i+1)
    else:
        return False
print(recursion(s,0))