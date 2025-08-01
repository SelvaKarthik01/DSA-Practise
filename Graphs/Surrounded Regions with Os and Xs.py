from collections import deque
n = int(input("Enter the No. of Rows : "))
m = int(input("Enter the No. of Columns : "))
grid = [[0]*m for _ in range(n)]
for i in range(n):
    for j in range(m):
        print("Grid[",i,"][",j,"]:",end = " ")
        grid[i][j] = input()
visited = [[0]*m for _ in range(n)]
def bfs(grid,visited):
    Queue = deque()
    for j in range(m):
        if grid[0][j] == "O":
            visited[0][j] = 1
            Queue.append([0,j])
    for i in range(n):
        if grid[i][m-1] == "O":
            visited[i][m-1] = 1
            Queue.append([i,m-1])
    for j in range(m-1,-1,-1):
        if grid[n-1][j] == "O":
            visited[n-1][j] = 1
            Queue.append([n-1,j]) 
    for i in range(n-1,-1,-1):
        if grid[i][0] == "O":
            visited[i][0] = 1
            Queue.append([i,0])
    while(len(Queue) != 0):
        i,j = Queue.popleft()
        if i+1 < n and grid[i+1][j] == "O" and visited[i+1][j] != 1:
            visited[i+1][j] = 1
            Queue.append([i+1,j])
        if i-1 >= 0 and grid[i-1][j] == "O" and visited[i-1][j] != 1:
            visited[i-1][j] = 1
            Queue.append([i-1,j])
        if j+1 < m and grid[i][j+1] == "O" and visited[i][j+1] != 1:
            visited[i][j+1] = 1
            Queue.append([i,j+1])
        if j-1 >= 0 and grid[i][j-1] == "O" and visited[i][j-1] != 1:
            visited[i][j-1] = 1
            Queue.append([i,j-1])
    for i in range(n):
        for j in range(m):
            if grid[i][j] == "O" and visited[i][j] != 1:
                grid[i][j] = "X"
bfs(grid,visited)
print(grid)

