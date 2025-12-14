"""
Docstring for Binary Search.Lower Bound of a Number

Smallest Index such that arr[ind] >= x

Time Complexity : O(logn)
Space Compleixty : O(1)

"""
def Binary_Search(L,target):
    low = 0 
    high = len(L)-1
    ans = len(L) # If no answer is present in the Array 
    while(low <= high):
        mid = low + (high-low)//2
        if L[mid] >= target:
            ans = mid 
            high = mid - 1
        else:
            low = mid + 1
    return ans
            

L = eval(input("Enter the List : "))
target = int(input("Enter the Target Element : "))
print(L[Binary_Search(L,target)])
