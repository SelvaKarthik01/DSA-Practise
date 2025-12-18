"""
Docstring for Binary Search.Find the Peal Element II

Time Complexity : O(nlogm)
Space Complexity : O(1)

"""
def MaxElement(matrix,mid):
    maxi = float("-inf")
    index = -1
    for i in range(len(matrix)):
        if matrix[i][mid] > maxi:
            maxi = matrix[i][mid]
            index = i 
    return index 
        
def Binary_Search(matrix):
    col = len(matrix[0])
    low = 0 
    high = col -1
    while(low <= high):
        mid = low + (high-low)//2
        row = MaxElement(matrix,mid)
        if mid-1 >= 0:
            left = matrix[row][mid-1]
        else:
            left = -1 
        if mid+1 < len(matrix[0]):
            right = matrix[row][mid+1]
        else:
            right = -1
        if left < matrix[row][mid] > right:
            return (matrix[row][mid],row,mid)
        elif left > matrix[row][mid]:
            high = mid - 1
        else:
            low = mid + 1
    return -1
matrix = [[4,2,5,1,4,5],[2,9,3,2,3,2],[1,7,6,0,1,3],[1,7,6,0,1,3],[3,6,2,3,7,2]]
print(Binary_Search(matrix))

