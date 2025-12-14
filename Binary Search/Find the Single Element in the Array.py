"""
Docstring for Binary Search.Find the Single Element in the Array

Time Complexity : O(logn)
Space Complexity : O(1)
"""
def Binary_Search(L):
    low = 0 
    high = len(L)-1
    while(low <= high):
        mid = low + (high-low)//2
        if low == high:
            return L[low]
        elif mid != 0 and L[mid] == L[mid-1]:
            if ((mid-low)+1) % 2 == 0:
                low = mid + 1
            else:
                high = mid -2
        elif mid != len(L)-1 and L[mid] == L[mid+1]:
            if ((mid+1-low)+1)%2 ==0:
                low = mid + 1 + 1
            else:
                high = mid -1
        else:
            return L[mid]
        

L = eval(input("Enter the List : "))
print(Binary_Search(L))
