# To Find the HCF or GCD of a Number 

a = int(input("Enter the value for a : "))
b = int(input("Enter the value for b : "))
def gcd(a,b):
    if (a==0):
        return b
    return gcd(b%a,a)
print(gcd(a,b))