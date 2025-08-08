class DisJointSet:
    def __init__(self,n):
        self.parent=[i for i in range(n+1)]
        self.size=[1]*(n+1)
    def findParent(self,node):
        if node == self.parent[node]:
            return node 
        else:
            self.parent[node] = self.findParent(self.parent[node])
            return self.parent[node]
    def UnionbySize(self,u,v):
        ulp_u = self.findParent(u)
        ulp_v = self.findParent(v)
        if ulp_u == ulp_v:
            return 
        elif self.size[ulp_v] > self.size[ulp_u]:
            self.parent[ulp_u] = ulp_v
            self.size[ulp_v] += self.size[ulp_u]
        else:
            self.parent[ulp_v] = ulp_u
            self.size[ulp_u] += self.size[ulp_v]

row = int(input("Enter the No. of Rows : "))
col = int(input("Enter the No. of Columns : "))
grid  = [[0]*col for _ in range(row)]
count=0
n = (row-1)*(col-1) + (col-1) + (row-1)
print(n)
Ds = DisJointSet(n)
for i in range(row):
    for j in range(col):
        print("Grid[",i,"][",j,"]: ",end = " ")
        grid[i][j] = int(input())
#grid = [[1, 1, 0, 1, 1], [1, 1, 0, 1, 1], [1, 1, 0, 1, 1], [0, 0, 1, 0, 0], [0, 0, 1, 1, 1], [0, 0, 1, 1, 1]]
print(grid)
visited=[[0]*col for _ in range(row)]
for i in range(row):
    for j in range(col):
        if grid[i][j] == 1 and visited[i][j] != 1:
            visited[i][j] = 1
            dr = [1,-1,0,0]
            dc = [0,0,1,-1]
            for delt in range(len(dr)):
                new_row = i + dr[delt]
                new_col = j + dc[delt]
                if new_row < row and new_col < col and new_row >= 0 and new_col >= 0:
                    if grid[new_row][new_col] == 1 and visited[new_row][new_col] == 1:
                        box = i*(col-1) + j + i 
                        neighbour_box = new_row*(col-1)+ new_col + new_row
                        Ds.UnionbySize(box,neighbour_box)
cost = 0
for i in range(row):
    for j in range(col):
        ulti_parents = set()
        if grid[i][j] == 0:
            dr = [1,-1,0,0]
            dc = [0,0,1,-1]
            for delt in range(len(dr)):
                new_row = i + dr[delt]
                new_col = j + dc[delt]
                if new_row < row and new_col < col and new_row >= 0 and new_col >= 0:
                    if grid[new_row][new_col] == 1:
                        box = new_row*(col-1) + new_col + new_row
                        ulti_parents.add(Ds.findParent(box))
        temp = 1
        for k in ulti_parents:
            temp += Ds.size[k]
        cost = max(cost,temp)
print("The Largest Island That could be Made is",cost)
        
            
                    
            
                    

            