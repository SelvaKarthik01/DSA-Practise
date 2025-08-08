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
import heapq
pq = []

n = int(input("Enter the No. of Nodes : "))
m = int(input("Enter the No. of Edges : "))
for i in range(m):
    s = input("Enter the Edge : ").split()
    weight = int(input("Enter the Edge Weight : "))
    heapq.heappush(pq,(weight,(int(s[0]),int(s[1]))))
Ds = DisjointSet(n)
sum = 0
mst = []
while(len(pq)!= 0):
    weight,temp = heapq.heappop(pq)
    u = temp[0]
    v = temp[1]
    if Ds.findParent(u) == Ds.findParent(v):
        continue
    else:
        Ds.UnionbySize(u,v)
        sum += weight
        mst.append((u,v,weight))

print("Minimum Weight for the Spanning tree using Kruskal's Algorithm is : ",sum)
print("MST : ",mst)
    

