"""
Docstring for Arrays.Set Matrix to 0

Set all the rows anc olumns of that box having 0 as 0 

Another apporach is store all the boxes which are having zeros and then based on the storing we convert the rows and columns will be 0 
TC -> O(n^2) -> for find ing the zeros and storing + O(n^2) for converting 
      Total -> O(2n^2) -> O(n^2)
SC -> O(n^2)

Another Approach instead of storing lets say we convert all the rows and columns as -1 inseatd of zero so that it doesnt interfere with original zeros 
TC -> O(n^3) -> to set all rows and columns as -1 + O(n^2) to convert all -1 to 0 back again 
      Total -> O(n^3) + O(n^2) -> O(n^3)
SC -> O(1)

Time Complexity : O(n^2) -> this is the min TC we could get as we need to oterate through the whole row 
Space Complexity : O(1)

"""
matrix = [[1,1,1,1],[1,0,1,1],[1,1,0,1],[0,1,1,1]] # One greater edge case where only the corner 1 shouldnt be changed 
rows = len(matrix)                                  # Changes thw precendence of which rows and columns to change first
columns = len(matrix[0])
col0 = 1
for i in range(rows):
    for j in range(columns):
        if matrix[i][j] == 0:
            if j != 0:
                matrix[0][j] = 0
            else:
                col0 = 0
            matrix[i][0] = 0
for i in range(rows-1,0,-1):
    for j in range(columns-1,0,-1):
        if matrix[i][0] == 0 or matrix[0][j] == 0:
            matrix[i][j] = 0 
for j in range(columns-1,0,-1):
    if matrix[0][0] == 0:
        matrix[0][j] = 0
for i in range(rows):
    if col0 == 0:
        matrix[i][0] = 0
print(matrix) 
            
            