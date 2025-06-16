# To find the XOR fo numebrs from 0 to a 
a = int(input("Enter the Number : "))
if a % 4 == 0:
    ans = a
elif a % 4 == 1:
    ans = 1
elif a % 4 == 2:
    ans = a + 1
else:
    ans = 0 
print(ans)

# If it given between a range of a and b 
def XOR(a):
    if a % 4 == 0:
        ans = a
    elif a % 4 == 1:
        ans = 1
    elif a % 4 == 2:
        ans = a + 1
    else:
        ans = 0 
    return ans
a = int(input("Enter the First Range : "))
b = int(input("Enter the Second Range :"))
print(XOR(a-1) ^ XOR(b))