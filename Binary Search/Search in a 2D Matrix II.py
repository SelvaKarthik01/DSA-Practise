"""
Docstring for Binary Search.Search in a 2D Matrix II

Only and Rows and Columsn are Sorted 

[1 4 7 11 15]            15,12,9 etc -> The lower Diagonal elements follow the sorted rule 
[2 5 8 12 19]
[3 6 9 16 22]
[10 13 14 17 24]
[18 21 23 26 30]

Time Compleixty : O(n+m)
Space Compleixty : O(1)

"""
def Binary_Search(matrix,target):
    row = 0 
    col = len(matrix[0])-1
    while(row < len(matrix) and col >= 0):
        if matrix[row][col] == target:
            return (row,col)
        elif matrix[row][col] < target:
            row += 1
        else:
            col -= 1
    return (-1,-1)

matrix =[[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[18,21,23,26,30]]
target = int(input("Enter the Target Element : "))
print(Binary_Search(matrix,target))
