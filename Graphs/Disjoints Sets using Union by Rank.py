# O(1) Constant Time Complexity 
class DisjointSet:
    def __init__(self,n):
        self.parent = [i for i in range(n+1)]
        self.rank = [0]*(n+1)
        self.size = [1]*(n+1)
    def findParent(self,node):
        if node == self.parent[node]:
            return node
        else:
            self.parent[node] = self.findParent(self.parent[node])
            return self.parent[node]
    def UnionbyRank(self,u,v):
        ulp_u = self.findParent(u)
        ulp_v = self.findParent(v)
        if self.rank[ulp_u] > self.rank[ulp_v]:
            self.parent[ulp_v] = ulp_u
        elif self.rank[ulp_v] > self.rank[ulp_u]:
            self.parent[ulp_u] = ulp_v
        elif self.rank[ulp_u] == self.rank[ulp_v]:
            self.parent[ulp_v] = ulp_u
            self.rank[ulp_u] += 1
    def UnionbySize(self,u,v):
        ulp_u = self.findParent(u)
        ulp_v = self.findParent(v)
        if self.size[ulp_v] > self.size[ulp_u]:
            self.size[ulp_v] += self.size[ulp_u]
            self.parent[ulp_u] = ulp_v
        else:
            self.size[ulp_u] += self.size[ulp_v]
            self.parent[ulp_v] = ulp_u
            
n = int(input("Enter the No. of Nodes : "))
Ds = DisjointSet(n)
m = int(input("Enter the No. of Edges"))
for i in range(m):
    s = input("Enter the Edges : ").split()
    Ds.UnionbySize(int(s[0]),int(s[1]))
u = int(input("Enter the First Node : "))
v = int(input("Enter the Second Node : "))
if Ds.findParent(u) == Ds.findParent(v):
    print("Same Component in the Graph ")
else:
    print("Different Components in the Graph ")
        
        