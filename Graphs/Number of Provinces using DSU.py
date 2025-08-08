class DisJointSet:
    def __init__(self,n):
        self.parent=[i for i in range(n+1)]
        self.size = [1]*(n+1)
    def findParent(self,node):
        if self.parent[node] == node:
            return node
        else:
            self.parent[node] = self.findParent(self.parent[node])
            return self.parent[node]
    def UnionbySize(self,u,v):
        ulp_u = self.findParent(u)
        ulp_v = self.findParent(v)
        if ulp_u == ulp_v:
            return
        elif self.size[ulp_u] > self.size[ulp_v]:
            self.parent[ulp_v] = ulp_u
            self.size[ulp_u] += self.size[ulp_v]
        else:
            self.parent[ulp_u] = ulp_v
            self.size[ulp_v] += self.size[ulp_u]
    def distinctBosses(self):
        count = 0
        for i in range(1,len(self.parent)):
            if i == self.parent[i]:
                count += 1
        return count
        
n = int(input("Enter the number of Nodes : "))
m = int(input("Enter the Number of Edges : "))
matrix = [[0]*(n+1) for _ in range(n+1)]
for i in range(n):
    matrix[i][i] = 0
for i in range(m):
    s = input("Enter the Edge : ").split()
    matrix[int(s[0])][int(s[1])]=1
    matrix[int(s[1])][int(s[0])]=1
print(matrix)
Ds = DisJointSet(n)
for i in range(n+1):
    for j in range(n+1):
        if matrix[i][j] == 1:
            if Ds.findParent(i) != Ds.findParent(j):
                Ds.UnionbySize(i,j)
print("Number of Distinct Provinces : ",Ds.distinctBosses())
                

    