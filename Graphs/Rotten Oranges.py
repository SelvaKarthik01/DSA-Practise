from collections import deque
n = int(input("Enter the No. of Rows in the Grid : "))
m = int(input("Enhter the No. of Columns in the Grid : "))
grid = [[0]*m for i in range(n)]
for i in range(n):
    for j in range(m):
        print("Grid[",i,"][",j,"] : ",end = " ")
        grid[i][j] = int(input())
visited = [[0]*m for i in range(n)]
def bfs(grid,visited):
    Queue = deque()
    n = len(grid)
    m = len(grid[0])
    for i in range(n):
        for j in range(m):
            if grid[i][j] == 2:
                Queue.append([i,j,0])
                visited[i][j] = 1
    t = 0
    tm = 0
    levelsize = len(Queue)
    while(len(Queue) != 0):
        nrow = Queue[0][0]
        ncol = Queue[0][1]
        ans = Queue.popleft()
        t = ans[2]
        tm = max(tm,t)
        if nrow+1 < n and grid[nrow+1][ncol] == 1 and visited[nrow+1][ncol] != 1:
            visited[nrow+1][ncol] = 1
            grid[nrow+1][ncol] = 2
            Queue.append([nrow+1,ncol,t+1])
        if nrow-1 >= 0 and grid[nrow-1][ncol] == 1 and visited[nrow-1][ncol] != 1:
            visited[nrow-1][ncol] = 1
            grid[nrow-1][ncol] = 2
            Queue.append([nrow-1,ncol,t+1])
        if ncol+1 < m and grid[nrow][ncol+1] == 1 and visited[nrow][ncol+1] != 1:
            visited[nrow][ncol+1] = 1
            grid[nrow][ncol+1] = 2
            Queue.append([nrow,ncol+1,t+1])
        if ncol-1 >= 0 and grid[nrow][ncol-1] == 1 and visited[nrow][ncol-1] != 1:
            visited[nrow][ncol-1] = 1
            grid[nrow][ncol-1] = 2
            Queue.append([nrow,ncol-1,t+1])
    for i in range(n):
        for j in range(m):
            if visited[i][j] == 0 and grid[i][j] == 1:
                return -1
    else:
        return tm
    
                
ans = bfs(grid,visited)
print(grid)
print("Minimum Time Required : ",ans)
