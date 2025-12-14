"""
Docstring for Binary Search.Binary Search

Time Complexity : O(logn) for every elemnent we are dividing teh search space by 2 so log base 2 n 
Space Complexity : O(1) 

"""
L = eval(input("Enter the List : "))
target = int(input("Enter the Target Element : "))
def Binary_Search(L,target):
    low = 0 
    high = len(L)-1
    while(low <= high):
        mid = low + (high-low)//2
        if L[mid] > target:
            high = mid -1
        elif L[mid] < target:
            low = mid + 1
        elif L[mid] == target :
            return mid 
    return -1 
print(Binary_Search(L,target))