n = int(input("Enter the Number N : "))
def recursion(n):
    if n<= 1:
        return n
    return recursion(n-1)+recursion(n-2)
print(recursion(n))