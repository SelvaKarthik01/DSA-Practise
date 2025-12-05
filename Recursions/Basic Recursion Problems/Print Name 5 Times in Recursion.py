name = input("Enter the Name to be Printed using Recursion : ")
n = int(input("Enter the Number N : "))
count=0
def recursion(name,n,count):
    if count == n:
        return 
    print(name)
    return recursion(name,n,count+1)
recursion(name,n,count)