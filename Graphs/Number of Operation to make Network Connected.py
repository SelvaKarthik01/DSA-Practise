class DisJointset:
    def __init__(self,n):
        self.parent = [i for i in range(n)]
        self.size = [1]*(n)
        self.extra_edges = 0
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
            self.extra_edges += 1
        elif self.size[ulp_v] > self.size[ulp_u]:
            self.parent[ulp_u] = ulp_v
            self.size[ulp_v] += self.size[ulp_u]
        else:
            self.parent[ulp_v] = ulp_u
            self.size[ulp_u] += self.size[ulp_v]
    def NumberofBosses(self):
        count = 0
        for i in range(len(self.parent)):
            if i == self.parent[i]:
                count += 1
        return count
n = int(input("Enter the Number of Nodes : "))
m = int(input("Enter the No. of Edges : "))
Ds = DisJointset(n)
for i in range(m):
    s = input("Enter the Edge : ").split()
    Ds.UnionbySize(int(s[0]),int(s[1]))
n_comp = Ds.NumberofBosses()
if Ds.extra_edges >= n_comp - 1 :
    print("Minimum No. of Operations are ",n_comp -1)
else:
    print("Connected Graph Creation not Possible !!")
    
    
    
    

            