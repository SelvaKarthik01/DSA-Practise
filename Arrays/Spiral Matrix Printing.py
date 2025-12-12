"""
Docstring for Arrays.Spiral Matrix Printing

Time Complexity : O(n^2) -> Just iterating thorugh the whole matrix 
Space Complexity : O(1) -> Just for variables 

"""

matrix = [[1,2,3,4,5,6],[20,21,22,23,24,7],[19,32,33,34,25,8],[18,31,36,35,26,9],[17,30,29,28,27,10],[16,15,14,13,12,11]]
rows = len(matrix)
cols = len(matrix[0])
top = 0 
left = 0 
bottom = rows-1 
right = cols-1
while(top <= bottom and left <= right):
    for i in range(left,right+1):
        print(matrix[top][i])
    top += 1
    for i in range(top,bottom+1):
        print(matrix[i][right])
    right -= 1
    if top <= bottom:
        for i in range(right,left-1,-1):
            print(matrix[bottom][i])
        bottom-=1
    if left <= right:
        for i in range(bottom,top-1,-1):
            print(matrix[i][left])
        left += 1

            