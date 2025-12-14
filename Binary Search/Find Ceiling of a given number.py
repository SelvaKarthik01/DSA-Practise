"""
Docstring for Binary Search.Find Ceiling of a given number

This is exact problem as finding the lower bound 
Ceil -> The Smallest Number that is >= Target 

Time Compleixty : O(logn)
Space Complexity : O(1)
"""
def Binary_Search(L,target):
    ans = -1 
    low = 0 
    high = len(L)-1
    while(low <= high):
        mid = low + (high-low)//2
        if L[mid] >= target:
            ans = mid 
            high = mid - 1
        else:
            low = mid + 1
    return L[ans]
            
L = eval(input("Enter the List : "))
target = int(input("Enter the target Element : "))
print(Binary_Search(L,target))
