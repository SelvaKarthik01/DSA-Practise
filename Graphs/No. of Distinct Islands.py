from collections import deque
n = int(input("Enter the No. of Rows in the Grid : "))
m = int(input("Enter the No. of Columns in the Grid : "))
grid = [[0]*m for _ in range(n)]
for i in range(n):
    for j in range(m):
        print("Grid[",i,"][",j,"]:",end = " ")
        grid[i][j] = int(input())
print(grid)
visited = [[0]*m for _ in range(n)]
shapes = []
def bfs(i,j,visited,grid,shapes):
    Queue = deque()
    visited[i][j] = 1
    Queue.append([i,j])
    shapes.append((i,j))
    while(len(Queue)!= 0):
        i,j = Queue.popleft()
        if i+1 < n and visited[i+1][j] != 1 and grid[i+1][j] == 1:
            visited[i+1][j] = 1
            Queue.append([i+1,j])
            shapes.append((i+1,j))
        if i-1 >= 0 and visited[i-1][j] != 1 and grid[i-1][j] == 1:
            visited[i-1][j] = 1
            Queue.append([i-1,j])
            shapes.append((i-1,j))
        if j+1 < m and visited[i][j+1] != 1 and grid[i][j+1] == 1:
            visited[i][j+1] = 1
            Queue.append([i,j+1])
            shapes.append((i,j+1))
            
        if j-1 >= 0 and visited[i][j-1] != 1 and grid[i][j-1] == 1:
            visited[i][j-1] = 1
            Queue.append([i,j-1])
            shapes.append((i,j-1))

count = 0 
final = []
for i in range(n):
    for j in range(m):
        if grid[i][j] == 1 and visited[i][j] != 1:
            shapes = []
            bfs(i,j,visited,grid,shapes)
            base = shapes[0]
            distinct = set()
            for k in shapes:
                t1 = k[0]-base[0]
                t2 = k[1]-base[1]
                distinct.add((t1,t2))
            for z in final:
                if distinct == z:
                    break
            else:
                final.append(distinct)

print("No. of Distinct Islands : ",len(final)) 
    
        