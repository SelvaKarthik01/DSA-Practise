n = int(input("Enter the Number N : "))
count = 0
def recursion(n,count):
    if count == n:   # Base Condition 
        return 
    print(count)
    count += 1
    return recursion(n,count) # Function Calling Itself 
recursion(n,count)
