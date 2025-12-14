"""
Docstring for Binary Search.Search in a Rotated Sorted Array II

Time Complexity : O(logn)
Space Compleixty : O(1)

"""
def Binary_Search(L,target):
    low = 0 
    high = len(L)-1
    while(low <= high):
        mid = low + (high-low)//2
        if L[mid]==target:
            return mid 
        elif L[low] == L[mid]==L[high]:
            low += 1
            high -=1
            continue
        elif L[low] <= L[mid]:
            if L[low] <= target <= L[mid]:
                high = mid - 1
            else:
                low = mid + 1
        else:
            if L[mid]  <= target <= L[high]:
                low = mid + 1
            else:
                high = mid - 1
    return -1
L = eval(input("Enter the List : "))
target = int(input("Enter the Target Element : '"))
print(Binary_Search(L,target))
