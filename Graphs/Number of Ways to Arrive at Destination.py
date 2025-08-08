n = int(input("Enter the Number of Cities : "))
m = int(input("Enter the Total Number of Roads : "))
from collections import defaultdict 
adj = defaultdict(set)
for i in range(m):
    s = input("Enter the Road between Cities : ")
    s= s.split()
    weight = int(input("Enter the Road Length : "))
    adj[int(s[0])].add((weight,int(s[1])))
    adj[int(s[1])].add((weight,int(s[0])))
print(adj)
import heapq
pq = []
src = int(input("Enter the Source City : "))
dest = int(input("Enter the Destination City : "))
distance = [float("inf")]*n 
ways = [0]*n
distance[src] = 0 
ways[src] += 1
heapq.heappush(pq,(distance[src],src))
while(len(pq)!=0):
    dist,node = heapq.heappop(pq)
    for j,i in adj[node]:
        if dist + j < distance[i]:
            distance[i] = dist + j
            heapq.heappush(pq,(distance[i],i))
            ways[i] = ways[node]
        elif dist + j == distance[i]:
            ways[i] += ways[node]
print(ways[dest])