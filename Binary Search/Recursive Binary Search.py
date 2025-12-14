"""
Docstring for Binary Search.Recursive Binary Search

Time Complexity : O(logn)
Space Complexity : O(1)
"""
def Binary_Search(L,target,low,high):
    if low > high:
        return -1
    mid = (low+high)//2
    if L[mid] == target:
        return mid 
    elif L[mid] > target:
        return Binary_Search(L,target,low,mid-1)
    else:
        return Binary_Search(L,target,mid+1,high)
L = eval(input("Enter the List : "))
target = int(input("Enter the Target Element : "))
print(Binary_Search(L,target,0,len(L)-1))