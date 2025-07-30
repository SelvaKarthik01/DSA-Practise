# In Other words to calculate the Number of components in a Graph 
from collections import defaultdict
n = int(input("Enter the Number of Nodes : "))
m = int(input("Enter the Number of Edges : "))
adj = defaultdict(set)
for i in range(m):
    s = input("Enter the Edge : ")
    s = s.split()
    adj[int(s[0])].add(int(s[1]))
    adj[int(s[1])].add(int(s[0]))
    
print(adj)
visited = []

def dfs(start,adj,visited):
    visited[start] = 1
    for i in adj[start]:
        if visited[i] != 1:        
            dfs(i,adj,visited)
            
for i in range(n+1):
    visited.append(0)
visited[0] = 1

start = int(input("Enter the Start Node : "))
dfs(start,adj,visited)
no_of_province= 1

for i in range(1,n+1):
    if visited[i] != 1:
        dfs(i,adj,visited)
        no_of_province += 1
print(no_of_province)

            


