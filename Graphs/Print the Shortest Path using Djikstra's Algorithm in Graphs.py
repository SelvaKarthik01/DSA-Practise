n = int(input("Enter the no. of Nodes in the Graph : "))
m = int(input("Enter the No. of Edges in the Graph : "))
from collections import defaultdict
import heapq
adj = defaultdict(set)
for i in range(m):
    s = input("Enter the Edge : ")
    s = s.split()
    weight = int(input("Enter the Edge Weight : "))
    adj[int(s[0])].add((weight,int(s[1])))
    adj[int(s[1])].add((weight,int(s[0])))
print(adj)
pq = []
distance = [float("inf")]*(n+1) 

src = int(input("Enter the Source Node : "))
dest = int(input("Enter the Destination Node : "))
parent = [0]*(n+1)
distance[src] = 0
parent[src] = src
heapq.heappush(pq,(0,src))
while(len(pq)!= 0):
    weight,node = heapq.heappop(pq)
    for i,j in adj[node]:
        if distance[node] + i < distance[j]:
            distance[j] = distance[node] + i 
            heapq.heappush(pq,(distance[j],j))
            parent[j] = node 
result = []
final_dest = dest
result.append(dest)
while(dest != src):
    dest = parent[dest]
    result.append(dest)
print(result)
print(parent)   
result.reverse()
print("The Shortest Path from the Source Node ",src," to the Destination Node ",final_dest," : ",end = " ")
for i in result:
    print(i,end = " ")
print()
print("Minimum Distance to be Covered : ",distance[final_dest])
    
    
    