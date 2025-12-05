n = int(input("Enter the Number N : "))
count = 1
def recursion(count,n):
    if count > n:
        return 
    recursion(count+1,n)
    print(count,end = " ")
recursion(count,n)