n = int(input("Enter the Number of Rows in the Grid : "))
m = int(input("Enter the Number of Columns in the Grid : "))
grid = [[0]*m for _ in range(n)]
for i in range(n):
    for j in range(m):
        print("Grid[",i,"][",j,"] : ",end = " ")
        grid[i][j] = int(input())
print(grid)
import heapq 
pq = []
distance = [[float("inf")]*m for _ in range(n)]
start = eval(input("Enter the Start Position in the Grid : "))
end = eval(input("Enter the End Position in the Grid : "))
distance[start[0]][start[1]]=0
heapq.heappush(pq,(0,(start[0],start[1])))
while(len(pq) != 0):
    weight,node = heapq.heappop(pq)
    row = node[0]
    col = node[1]
    if row + 1 < n and grid[row+1][col] == 1 and distance[row][col] + 1 < distance[row+1][col]:
        distance[row+1][col] = distance[row][col] + 1
        heapq.heappush(pq,(distance[row+1][col],(row+1,col)))
    if row - 1 >= 0 and grid[row-1][col] == 1 and distance[row][col] + 1 < distance[row-1][col]:
        distance[row-1][col] = distance[row][col] +1 
        heapq.heappush(pq,(distance[row-1][col],(row-1,col)))
    if col +1 < m  and grid[row][col+1] == 1 and distance[row][col] + 1 < distance[row][col+1]:
        distance[row][col+1] = distance[row][col] +1 
        heapq.heappush(pq,(distance[row][col+1],(row,col+1)))
    if col - 1 >= 0 and grid[row][col-1] == 1 and distance[row][col] + 1 < distance[row][col-1]:
        distance[row][col-1] = distance[row][col] +1 
        heapq.heappush(pq,(distance[row][col-1],(row,col-1)))
print("Shortest Distance to Travle given the Start and End Coordinates is : ",distance[end[0]][end[1]])
        
        