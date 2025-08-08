n = int(input("Enter the No. of Rows : "))
m = int(input("Enter the No. of Columns : "))
grid = [[float("inf")]*m for _ in range(n)]
for i in range(m):
    s = input("Enter the Edge : ")
    s = s.split()
    weight = int(input("Enter the Weight : "))
    grid[int(s[0])][int(s[1])]=weight 
for i in range(n):
    grid[i][i] = 0
for k in range(n):
    for i in range(n):
        for j in range(m):
            grid[i][j] = min(grid[i][j],grid[i][k]+grid[k][j])
ans = 0
for i in range(n):
    for j in range(m):
        if grid[i][i] < 0:
            ans = -1
            break
if ans == 0 :
    for i in range(n):
        for j in range(m):
            print(grid[i][j],end = " ")
        print() 
elif ans == -1:
    print("Negative Edge Cycle Detected !!")

            