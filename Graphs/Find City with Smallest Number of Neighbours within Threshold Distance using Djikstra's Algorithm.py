n = int(input("Enter the No. of Cities : "))
m = int(input("Enter the No. of Roads : "))
from collections import defaultdict
adj = defaultdict(set)
for i in range(m):
    s = input("Enter the Edge").split()
    weight = int(input("Enter the Road length : "))
    adj[int(s[0])].add((weight,int(s[1])))
    adj[int(s[1])].add((weight,int(s[0])))
print(adj)
threshold = int(input("Enter the Threshold Distance : "))
result = [[] for _ in range(n)]
import heapq
for i in range(n):
    distance = [float("inf")]*n 
    distance[i] = 0
    pq = []
    heapq.heappush(pq,(distance[i],i))
    while(len(pq) != 0):
        dist,node = heapq.heappop(pq)
        for k,j in adj[node]:
            if dist + k < distance[j]:
                distance[j] = dist + k 
                heapq.heappush(pq,(distance[j],j))
    for z in distance:
        if z <= threshold:
            result[i].append(z)
min_length = float("inf")
ans = []
for i in range(len(result)):
    if len(result[i]) < min_length:
        ans = [i]
        min_length = len(result[i])
    elif len(result[i]) == min_length:
        ans.append(i)
print(max(ans))
        
     