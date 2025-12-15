"""
Docstring for Binary Search.Find the Peak element

arr[i-1] < arr[i] < arr[i+1]

Time Complexity : O(logn)
Space Complexity : O(1)

"""
def Binary_Search(L):
    if L[0] > L[1]:
        return 1
    elif L[-1] > L[-2]:
        return len(L)-1
    else:
        low = 1
        high = len(L)-1
        while(low <= high):
            mid = low + (high-low)//2
            if L[mid-1] < L[mid] > L[mid+1]:
                return mid 
            elif L[mid-1] < L[mid]:
                low = mid + 1
            else:               # This makes sure it holds true for multiple Peaks too [1,5,1,2,1]
                high = mid -1 

L = eval(input("Enter the List : "))
print(L[Binary_Search(L)])
