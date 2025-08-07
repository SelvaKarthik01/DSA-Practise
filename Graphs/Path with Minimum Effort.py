n = int(input("Enter the No. of Rows in Grid :" ))
m = int(input("Enter the No. of Columns in Grid : "))
import heapq
grid = [[0]*m for _ in range(n)]
for i in range(n):
    for j in range(m):
        print("Grid[",i,"][",j,"]: ",end = " ")
        grid[i][j] = int(input())
distance = [[float("inf")]*m for _ in range(n)]
distance[0][0] = 0 
pq = []
heapq.heappush(pq,(distance[0][0],(0,0)))
ans = -1
while(len(pq) != 0):
    dist,temp = heapq.heappop(pq)
    row = temp[0]
    col = temp[1]
    print(row,col)
    if row == n-1 and col == n-1:
        break
    if row + 1 < n :
        new_dist = max(dist,abs(grid[row][col] - grid[row+1][col]))
        if new_dist < distance[row+1][col]:
            distance[row+1][col] = new_dist
            heapq.heappush(pq,(new_dist,(row+1,col)))
    if row - 1 >= 0 :
        new_dist = max(dist,abs(grid[row][col] - grid[row-1][col]))
        if new_dist < distance[row-1][col]:
            distance[row-1][col] = new_dist
            heapq.heappush(pq,(new_dist,(row-1,col)))
    if col + 1 < m :
        new_dist = max(dist,abs(grid[row][col] - grid[row][col+1]))
        if new_dist < distance[row][col+1]:
            distance[row][col+1] = new_dist
            heapq.heappush(pq,(new_dist,(row,col+1)))
    if col - 1 >= 0:
        new_dist = max(dist,abs(grid[row][col] - grid[row][col-1]))
        if new_dist < distance[row][col-1]:
            distance[row][col-1] = new_dist
            heapq.heappush(pq,(new_dist,(row,col-1)))
print("The Path with Minimum Effort is : ",distance[n-1][m-1])
        