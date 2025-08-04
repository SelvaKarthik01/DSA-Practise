n = int(input("Enter the Number of Nodes : "))
m = int(input("Enter the Number of Edges : "))
from collections import defaultdict
adj = defaultdict(set)
for i in range(m):
    s = input("Enter the Edge : ")
    s = s.split()
    adj[int(s[0])].add(int(s[1]))
print(adj)
visited = [0]*(n+1)
stack = []

def dfs(node,adj,visited,stack):
    visited[node] = 1
    for i in adj[node]:
        if visited[i] != 1:
            dfs(i,adj,visited,stack)
    stack.append(node)
for i in range(1,n+1):
    if visited[i] != 1:
        dfs(i,adj,visited,stack)
print("Topological Sort : ",end = " ")
while(len(stack) != 0):
    print(stack.pop(),end = " ")
