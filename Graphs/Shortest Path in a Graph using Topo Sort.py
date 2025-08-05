n = int(input("Enter the Number of Nodes in the Graph : "))
m = int(input("Enter the Number of Edges in the Graph : "))
from collections import defaultdict
adj = defaultdict(set)
for i in range(m):
    s = input("Enter the Edge : ")
    s = s.split()
    weight = int(input("Enter the Edge Weight : "))
    adj[int(s[0])].add((int(s[1]),weight))
print(adj)

def dfs(node,adj,visited,stack):
    visited[node] = 1
    for i,j in adj[node]:
        if visited[i] != 1:
            dfs(i,adj,visited,stack)
    stack.append(node)
visited = [0]*(n)
stack = []
for i in range(n):
    if visited[i] != 1:
        dfs(i,adj,visited,stack)
distance = [float("inf")]*n 
src = int(input("Enter the Source Node : "))
distance[src] = 0 
while(len(stack) != 0):
    node = stack.pop()
    for i,j in adj[node]:
        if distance[node] + j < distance[i]:
            distance[i] = distance[node] + j 
print("The Shortest Paths from the Source Node ",src,": ",end = " ")
for i in range(len(distance)):
    print(distance[i],end = " ")
    