"""
Docstring for Binary Search.Minimum in a Rotated Sorted Array

Time Complexity : O(logn)
Space Compleixty : O(1)

One Edge Case failing if we check left part as sorted or not [7,8,9,1,2,3,4,5,6]
"""

def Binary_Search(L):
    ans = float("inf")
    low = 0 
    high = len(L)-1
    while(low <= high):
        mid = low + (high-low)//2
        if L[low] == L[mid] == L[high]:
            low += 1
            high -= 1
            continue 
        elif L[low] <= L[mid]:
            ans = min(ans,L[low])
            low = mid + 1
        else:
            ans = min(ans,L[mid])
            high = mid - 1 
    return ans  
L = eval(input("Enter the List : "))
print(Binary_Search(L,))

