n = int(input("Enter the Number N : "))
def recursion(n,sum):
    if n == 0:
        print(sum)
        return
     
    return recursion(n-1,sum+n)
sum = 0 
recursion(n,sum)
 

n = int(input("Enter the Number using Backtracking : "))
sum = 0
def recursion(n,sum):
    if n == 0:
        return 0
    sum = recursion(n-1,sum)
    return sum+n
print(recursion(n,sum))
