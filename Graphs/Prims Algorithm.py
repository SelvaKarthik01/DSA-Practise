n = int(input("Enter the No. of Nodes : "))
m = int(input("Enter the No. of Edges : "))
from collections import defaultdict
adj = defaultdict(set)
for i in range(m):
    s = input("Enter the Edges : ").split()
    weight = int(input("Enter the Weight of the Edge : "))
    adj[int(s[0])].add((weight,int(s[1])))
    adj[int(s[1])].add((weight,int(s[0])))
print(adj)
import heapq
visited = [0]*n
mst = []
pq = []
sum = 0

heapq.heappush(pq,(0,(0,-1)))
while(len(pq)!= 0):
    weight,temp = heapq.heappop(pq)
    node = temp[0]
    parent = temp[1]
    if visited[node] != 1:
        visited[node] = 1
        mst.append((parent,node))
        sum += weight
        for j,i in adj[node]:
            heapq.heappush(pq,(j,(i,node)))
print("Minimum Weight of the Spanning Tree is : ",sum)
print("MST : ",mst)
        
        