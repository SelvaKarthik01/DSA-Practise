class DisJointSet:
    def __init__(self,n):
        self.parent=[i for i in range(n)]
        self.size = [1]*(n)
        self.count = 0
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
            self.count += 1
        elif self.size[ulp_v] > self.size[ulp_u]:
            self.parent[ulp_u] = ulp_v
            self.size[ulp_v] += self.size[ulp_u]
        else:
            self.parent[ulp_v] = ulp_u
            self.size[ulp_u] += self.size[ulp_v]
        

row = int(input("Enter the no. of Rows : "))
col = int(input("Enter the Number of Columns : "))
count = 0 
matrix = []
for i in range(row):
    for j in range(col):
        matrix.append(count)
        count += 1
n = (row-1)*(col-1) + (col-1) + (row-1)

visited=[0]*n
print(visited)
Ds = DisJointSet(n)
m = int(input("Enter the Number of Queries : "))
result = []
for i in range(m):
    s = eval(input("Enter the Query : "))
    box = s[0]*(col-1) + s[1] + s[0]
    if visited[box] != 1:
        visited[box] = 1
        Ds.count += 1
        dr = [0,0,-1,1]
        dc = [-1,1,0,0]
        for j in range(len(dr)):
            new_row = s[0] + dr[j]
            new_col = s[1] + dc[j] 
            if new_row < row and new_col < col and new_row >= 0 and new_col >= 0:
                neighbour_box = new_row*(col-1) + new_col + new_row
                if visited[neighbour_box] == 1:
                    print("Neighbour ",neighbour_box)
                    Ds.count -= 1
                    Ds.UnionbySize(box,neighbour_box)
    print(Ds.count)
                    
    result.append(Ds.count)
print("Final Query Result : ",result)
    
                
            
        
    


