"""
Docstring for Binary Search.Koko Eating Bananas
"""
import math
def TimeTaken(L,n):
    time = 0 
    for i in L:
        time += math.ceil(i/n)
    return time
        
    
def Binary_Search(L,h):
    low = 1 
    high = L[-1]
    ans = -1
    while(low<=high):
        mid = low + (high-low)//2
        if TimeTaken(L,mid) <= h:
            ans = mid
            high = mid -1 
        else:
            low = mid + 1
    return ans  # Return low 
L = eval(input("Enter the Pile of Bananas : "))
h = int(input("Enter the Maximum Time Limit : "))
print(Binary_Search(L,h))