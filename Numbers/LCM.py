a = int(input("Enter the value for a  : "))
b = int(input("Enter the avlue for b : "))
def gcd(a,b):
    if a == 0 :
        return b
    return gcd(b%a,a)
ans = a * b // gcd(a,b)
print(ans)