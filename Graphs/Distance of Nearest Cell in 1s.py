from collections import deque 
n = int(input("Enter the No. of Rows : "))
m = int(input("Enter the No. of Columns : "))
grid = []
grid = [[0]*m for _ in range(n)]
for i in range(n):
    for j in range(m):
        print("Grid[",i,"][",j,"] : ",end= " ")
        grid[i][j] = int(input())
print(grid)
visited = [[0]*m for _ in range(n)]
ans = [[0]*m for _ in range(n)]

def bfs(visited,grid,ans):
    Queue = deque()
    for i in range(n):
        for j in range(m):
            if grid[i][j] == 1:
                Queue.append([i,j,0])
                ans[i][j] = 0
                visited[i][j] = 1
    while(len(Queue)):
        temp = Queue.popleft()
        i = temp[0]
        j = temp[1]
        t = temp[2]
        if i+1 < n and visited[i+1][j] != 1:
            visited[i+1][j] = 1
            ans[i+1][j] = t + 1
            Queue.append([i+1,j,ans[i+1][j]])
        if i-1 >= 0 and visited[i-1][j] != 1:
            visited[i-1][j] = 1
            ans[i-1][j] = t + 1
            Queue.append([i-1,j,ans[i-1][j]])
        if j+1 < m and visited[i][j+1] != 1:
            visited[i][j+1] = 1
            ans[i][j+1] = t + 1
            Queue.append([i,j+1,ans[i][j+1]])
        if j-1 >= 0 and visited[i][j-1] != 1:
            visited[i][j-1] = 1
            ans[i][j-1] = t + 1
            Queue.append([i,j-1,ans[i][j-1]])
bfs(visited,grid,ans)
print("Answer Grid : ",end = " ")
print(ans)