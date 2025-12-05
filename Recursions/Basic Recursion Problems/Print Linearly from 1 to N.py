n = int(input("Enter the Number N : "))
def recursion(count,n):
    if count == n+1:
        return 
    print(count,end = " ")
    return recursion(count+1,n)
count = 1
recursion(count,n)