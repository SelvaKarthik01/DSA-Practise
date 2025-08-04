from collections import defaultdict
adj = defaultdict(set)
n = int(input("Enter the No. of Nodes in the Graph : "))
m = int(input("Enter the No. of Edges in the Graph : "))
for i in range(m):
    s = input("Enter the Edge : ")
    s = s.split()
    adj[int(s[0])].add(int(s[1]))
print(adj)
visited = [0]*(n+1)


def dfs(node,adj,visited,path_vis):
    visited[node] = 1
    path_vis[node] = 1
    for i in adj[node]:
        if visited[i] != 1:
            if dfs(i,adj,visited,path_vis) == True:
                return True 
        elif visited[i] == 1 and path_vis[i] == 1:
            return True 
    path_vis[node] = 0
    return False;
                
            

for i in range(1,n+1):
    if visited[i] != 1:
        if dfs(i,adj,visited,path_vis) == True:
            print("Cycle Detected in graph !!")
            break
else:
    print("No cycle Detected in graph !!")