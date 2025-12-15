"""
Docstring for Binary Search.Find the Nth Root of a Number

Time Complexity : O(logn)
Space Complexity : O(1)
"""
def Binary_Search(n,m):
    low = 0 
    high = m
    while(low <= high):
        mid = low + (high-low)//2
        if (mid**n) == m:
            return True 
        elif (mid**n) > m:
            high = mid-1
        else:
            low = mid + 1
    return False 

m = int(input("Enter the Number : "))
n = int(input(("Enter the Root : ")))
print(Binary_Search(n,m))