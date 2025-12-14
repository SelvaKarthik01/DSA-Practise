"""
Docstring for Binary Search.Find the Number of Rotations of a Rotated Sorted Array

Time Complexity : O(logn)
Space Complexity : O(1)

"""
def Binary_Search(L):
    result = -1
    ans = float("inf")
    low = 0 
    high = len(L)-1
    while(low <= high):
        mid = low + (high-low)//2
        if L[low] <= L[mid]:
            if L[low] < ans:
                ans = L[low]
                result = low
            low = mid + 1
        else:
            if ans > L[mid]:
                ans = L[mid]
                result = mid 
            high = mid -1
    print(ans)
    return result
     

L = eval(input("Enter the List : "))
print(Binary_Search(L))
    
    