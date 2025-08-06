n = int(input("Enter the Number of Nodes : "))
m = int(input("Enter the No. of Edges : "))
from collections import defaultdict
adj = defaultdict(set)
for i in range(m):
    s = input("Enter the Edge : ")
    weight = int(input("Enter trthe Edge Weight : "))
    s = s.split()
    adj[int(s[0])].add((weight,int(s[1])))
    adj[int(s[1])].add((weight,int(s[0])))
print(adj)
distance = [(float("inf"))]*n 
src = int(input("Enter the Source Node : "))
distance[src] = 0
import heapq 
pq = []
heapq.heappush(pq,(0,src))
while(pq):
    weight,node = heapq.heappop(pq)
    for i,j in adj[node]:
        if distance[node] + i < distance[j]:
            distance[j] = distance[node] + i
            heapq.heappush(pq,(distance[j],j))
print("The Shortest Paths to All Nodes from the Source Node ",src," : ")
for i in range(len(distance)):
    print(i,"--> ",distance[i])
    