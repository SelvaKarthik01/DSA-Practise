n = int(input("Enter the Number N : "))
def recursion(n):
    if n == 0:
        return 
    recursion(n-1)
    print(n,end = " ")
recursion(n)