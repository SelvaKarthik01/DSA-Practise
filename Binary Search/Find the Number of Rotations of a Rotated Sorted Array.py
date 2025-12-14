"""
Docstring for Binary Search.Find the Number of Rotations of a Rotated Sorted Array

Time Complexity : O(logn)
Space Complexity : O(1)

"""
def Binary_Search(L):
    low = 0
    high = len(L) - 1

    while low <= high:
        # already sorted → smallest is at low
        if L[low] <= L[high]:
            return low

        mid = low + (high - low) // 2

        # mid is the minimum
        if mid > 0 and L[mid] < L[mid - 1]:
            return mid

        # decide direction using HIGH, not LOW
        if L[mid] > L[high]:
            low = mid + 1
        else:
            high = mid - 1
     

L = eval(input("Enter the List : "))
print(Binary_Search(L))
    
    