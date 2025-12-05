n = int(input("Enter the number N : "))
def recursion(n):
    if n == 0:
        return 
    print(n,end = " ")
    return recursion(n-1)
recursion(n)