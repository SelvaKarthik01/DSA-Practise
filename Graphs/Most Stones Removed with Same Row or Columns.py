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
        if self.size[ulp_v] > self.size[ulp_u]:
            self.parent[ulp_u] = ulp_v
            self.size[ulp_v] += self.size[ulp_u]
        else:
            self.parent[ulp_v] = ulp_u
            self.size[ulp_u] += self.size[ulp_v]
    def Distinctbosses(self,stones):
        n_components_size=[]
        parents = set()
        for stone in stones:
            parents.add(self.findParent(stone))
        for i in parents:
            if self.size[i] != 1:
                n_components_size.append(self.size[i] -1)
        
        return n_components_size
                
row = int(input("Enter the No. of Rows in Grid : "))
col = int(input("Enter the No. of Columns in Grid : "))
n = (row-1)*(col-1)+(col-1)+(row-1)
print(n)
grid = [[0]*col for _ in range(row)]
Ds = DisJointSet(n)
m = int(input("Enter the Number of Stones : "))
for i in range(m):
    coord = eval(input("Enter the Coordinates : "))
    grid[coord[0]][coord[1]]= 1
distinct_parents=set()
for i in range(row):
    for j in range(col):
        if grid[i][j] == 1 :
            box = i * (col-1) + j + i
            distinct_parents.add(box)

            rows = grid[i]
            cols = []
            for k in range(row):
                cols.append(grid[k][j])
            for one_rows in range(len(rows)):
                if rows[one_rows] == 1:
                    n_box = i*(col-1) + one_rows + i
                    Ds.UnionbySize(box,n_box)
            for one_cols in range(len(cols)):
                if cols[one_cols] == 1:
                    n_box = one_cols*(col-1) + j + one_cols
                    Ds.UnionbySize(box,n_box)
print(distinct_parents)
print(Ds.parent)
print(Ds.size)
print("Number of Stones that Can be Removed are : ",sum(Ds.Distinctbosses(distinct_parents)))
    
            
            
    