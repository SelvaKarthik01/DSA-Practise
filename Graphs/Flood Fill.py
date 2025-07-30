from collections import deque
grid = []
n = int(input("Enter the No. of Rows in Grid : "))
m = int(input("Enter the No. of Columns oin Grid : "))
for i in range(n):
    temp = []
    for j in range(m):
        temp.append(0)
    grid.append(temp)
for i in range(n):
    for j in range(m):
        print("Grid[",i,"][",j,"] : ",end = " ")
        grid[i][j] = int(input())
print(grid)
sr = int(input("Enter the Starting Row : "))
sc = int(input("Enter the Starting Column : "))
init = grid[sr][sc]
newcolor = int(input("Enter the New Color : "))
visited = []
for i in range(n):
    temp = []
    for j in range(m):
        temp.append(0)
    visited.append(temp)

def bfs(i,j,visited,newcolor,init,grid):
    visited[i][j] = 1
    n = len(grid)
    m = len(grid[0])
    grid[i][j] = newcolor
    Queue = deque()
    Queue.append([i,j])
    while(len(Queue)!= 0):
        nrow = Queue[0][0]
        ncol = Queue[0][1]
        Queue.popleft()
        if ncol+1 < m and grid[nrow][ncol+1] == init and visited[nrow][ncol+1] != 1:
            visited[nrow][ncol+1] = 1
            grid[nrow][ncol+1] = newcolor
            Queue.append([nrow,ncol+1])
        if ncol-1 >= 0 and grid[nrow][ncol-1] == init and visited[nrow][ncol-1] != 1:
            visited[nrow][ncol-1] = 1
            grid[nrow][ncol-1] = newcolor
            Queue.append([nrow,ncol-1])
        if nrow-1 >= 0 and grid[nrow-1][ncol] == init and visited[nrow-1][ncol] != 1:
            visited[nrow-1][ncol] = 1
            grid[nrow-1][ncol] = newcolor
            Queue.append([nrow-1,ncol])
        if nrow+1 < n and grid[nrow+1][ncol] == init and visited[nrow+1][ncol] != 1:
            visited[nrow+1][ncol] = 1
            grid[nrow+1][ncol] = newcolor
            Queue.append([nrow+1,ncol])

bfs(sr,sc,visited,newcolor,init,grid)
print(grid)



    
    
                
        