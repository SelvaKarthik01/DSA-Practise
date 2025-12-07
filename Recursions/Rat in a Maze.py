"""
Docstring for Recursions.Rat in a Maze

Consider a rat placed at position (0, 0) in an n x n square matrix maze[][]. The rat's goal is to reach the destination at position (n-1, n-1). The rat can move in four possible directions: 'U'(up), 'D'(down), 'L' (left), 'R' (right).

The matrix contains only two possible values:

0: A blocked cell through which the rat cannot travel.
1: A free cell that the rat can pass through.
Your task is to find all possible paths the rat can take to reach the destination, starting from (0, 0) and ending at (n-1, n-1), under the condition that the rat cannot revisit any cell along the same path. Furthermore, the rat can only move to adjacent cells that are within the bounds of the matrix and not blocked.
If no path exists, return an empty list.

Note: Return the final result vector in lexicographically smallest order.

Examples:

Input: maze[][] = [[1, 0, 0, 0], [1, 1, 0, 1], [1, 1, 0, 0], [0, 1, 1, 1]]
Output: ["DDRDRR", "DRDDRR"]
Explanation: The rat can reach the destination at (3, 3) from (0, 0) by two paths - DRDDRR and DDRDRR, when printed in sorted order we get DDRDRR DRDDRR.
Input: maze[][] = [[1, 0], [1, 0]]
Output: []
Explanation: No path exists as the destination cell (1, 1) is blocked.
Input: maze[][] = [[1, 1, 1], [1, 0, 1], [1, 1, 1]]
Output: ["DDRR", "RRDD"]
Explanation: The rat has two possible paths to reach the destination: DDRR and RRDD.
Constraints:
2 ≤ n ≤ 5
0 ≤ maze[i][j] ≤ 1


"""

#maze = eval(input("Enter the Maze : "))
maze=[[1, 0, 0, 0], [1, 1, 0, 1], [1, 1, 0, 0], [0, 1, 1, 1]]
ans =[]
n = len(maze)
visited = [[0 for _ in range(n) ]for _ in range(n)]
def recursion(maze,row,col,visited,path,ans):
    if row == len(maze)-1 and col == len(maze)-1:
        ans.append(list(path))
        return 
    # Going Down   # In this Specific order for lexicographically osrtuiung the final paths 
    if row +1 < len(maze) and maze[row+1][col] == 1 and visited[row+1][col] == 0:
        path.append("D")
        visited[row+1][col] = 1
        recursion(maze,row+1,col,visited,path,ans)
        visited[row+1][col] = 0 
        path.pop()
    # Going Left
    if col - 1 >= 0 and maze[row][col-1] == 1 and visited[row][col-1] == 0:
        path.append("L")
        visited[row][col-1] =1 
        recursion(maze,row,col-1,visited,path,ans)
        visited[row][col-1] = 0 
        path.pop()
    # Going Right 
    if col + 1 < len(maze) and maze[row][col+1] == 1 and visited[row][col+1] == 0:
        path.append("R")
        visited[row][col+1] =1 
        recursion(maze,row,col+1,visited,path,ans)
        visited[row][col+1] = 0 
        path.pop()
    # Going Up
    if row - 1 >= 0 and maze[row-1][col] == 1 and visited[row-1][col] == 0:
        path.append("U")
        visited[row-1][col] = 1
        recursion(maze,row-1,col,visited,path,ans)
        visited[row-1][col] = 0 
        path.pop()
    return 
recursion(maze,0,0,visited,[],ans)
print("Possible Paths : ",ans)
    
        