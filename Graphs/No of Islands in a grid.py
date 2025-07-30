from collections import deque
grid = []

n = int(input("Enter the No. of Rows of Grid : "))
m = int(input("Enter the No. of Columns of Grid : "))
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

def bfs(i,j,visited,grid):
    n = len(grid)
    m = len(grid[0])
    Queue = deque()
    visited[i][j] = 1
    Queue.append([i,j])
    while(len(Queue) != 0):
        row = Queue[0][0]
        col = Queue[0][1]
        Queue.popleft()
        for delta in range(-1,2):
            for gamma in range(-1,2):
                nrow = row + delta
                ncol = col + gamma 
                if nrow >= 0 and nrow < n and ncol >= 0 and ncol< m and visited[nrow][ncol] != 1 and grid[nrow][ncol] == 1:
                    Queue.append([nrow,ncol])
                    visited[nrow][ncol] = 1 
                    
                    
visited = []
for i in range(n):
    temp = []
    for j in range(m):
        temp.append(0)
    visited.append(temp)

count = 0
for i in range(n):
    for j in range(m):
        if (visited[i][j] != 1 and grid[i][j] == 1):
            count += 1
            bfs(i,j,visited,grid)
print("No. of Islands in grid : ",count)
            
        