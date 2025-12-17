"""
Docstring for Binary Search.Find the Row with Maximum 1s

Only Possible if we have a sorted row

Time Complexity : O(n)*O(logn) -> O(nlogn)
Space Complexity : O(1)

"""
def Binary_Search(L):
    low = 0 
    high = len(L)-1
    ans = len(L)
    while(low<= high):
        mid = low + (high-low)//2
        if L[mid] == 1:
            ans = mid 
            high = mid -1 
        else:
            low = mid + 1
    return len(L)-ans
matrix = [[0,0,1,1,1],[0,0,0,0,0],[0,1,1,1,1],[0,0,0,0,0],[0,1,1,1,1]]
maxi = 0 
index = -1
for row in range(len(matrix)):
    count = Binary_Search(matrix[row])
    if  count > maxi:
        index = row 
        maxi = count
print("Maximum Number of 1s in a Row :  ",maxi)
    
