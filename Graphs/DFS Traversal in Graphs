from collections import defaultdict
print("Undirected Graph")
n = int(input("Enter the Number of Nodes : "))
m = int(input("Enter the Number of Edges : "))
adj = defaultdict(set)
for i in range(m):
    s = input("Enter the Edge : ")
    s = s.split()
    adj[int(s[0])].add(int(s[1]))
    adj[int(s[1])].add(int(s[0]))
print(adj)

def dfs(node,adj,visited,ans):
    visited[node] = 1
    ans.append(node)
    for i in adj[node]:
        if visited[i] != 1:
            dfs(i,adj,visited,ans)
            
start = int(input("Enter the Starting node for BFS : "))

visited = []
for i in range(n+1):
    visited.append(0)
ans = []
dfs(start,adj,visited,ans)
print("DFS -> ",ans)


            
    
    
    



    
    
        