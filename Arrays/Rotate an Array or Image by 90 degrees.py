"""
Docstring for Arrays.Rotate an Array or Image by 90 degrees

[1 2 3 4]                    [13 9 5 1]
[5 6 7 8]          --->      [14 10 6 2]
[9 10 11 12]                 [15 11 7 3]
[13 14 15 16]                [16 12 8 4]

Have a ans matrix start iertaing through the matrx and keep matrix[i][j] -> ans[j][n-1-i]
TC -> O(n^2)
SC -> O(n^2)

Algorithm after observing and finding patterns:

1) Find the transpose 
for i in range(rows):
    for j in range(i+1,cols):
        matrix[i][j],matrix[j],[i] = matrix[j][i],matrix[i][j]
2) and Reverse each row after transposing

Time Complexity : O(n^2) -> for transposing the matrix  + O(n^2) -> reversing the rows
                  Total -> O(n^2) + O(n^2) -> O(2n^2) -> O(n^2)
Space Complexity : O(1)

"""
matrix=[[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]
rows = len(matrix)
cols = len(matrix[0])
for i in range(rows):
    for j in range(cols):
        if i != j:
            matrix[i][j],matrix[j][i] = matrix[j][i],matrix[i][j]
        else:
            break
for i in range(rows):
    matrix[i].reverse()
print(matrix)
