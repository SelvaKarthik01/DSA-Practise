"""
Docstring for Binary Search.Search in a 2D Matrix

Every Row is been Sorted

Row -> mid/col
Col -> mid % col

<----4---->                   6 -> 6//4 -> 1   6%4 -> 2
[3 4 6 8]          0
[10 12 13 15]      1
[17 18 19 20]      2

Time Complexity : O(log(n*m))
Space Complexity : O(1)

"""
def Binary_Search(matrix,target):
    low = 0 
    high = (len(matrix[0])*len(matrix))-1
    col=len(matrix[0])
    while(low <= high):
        mid = low + (high - low)//2
        if matrix[mid//col][mid%col] == target:
            return (mid//col,mid%col)
        elif matrix[mid//col][mid%col] > target:
            high = mid -1 
        else:
            low = mid + 1
    return (-1,-1)
matrix = [[3,4,6,8],[10,12,13,15],[17,18,19,20]]
target = int(input("Enter the Target Element : "))
print(Binary_Search(matrix,target))



 