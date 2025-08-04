# Safe Nodes are those nodes whose all paths always lead to a termonal node that is a node with zero outdegress
n = int(input("Enter the No.of Nodes in graph "))
m = int(input("Enter the No. of Edges in the Graph : "))
from collections import defaultdict
adj = defaultdict(set)
for i in range(m):
    s = input("Enter the Edges : ")
    s = s.split()
    adj[int(s[0])].add(int(s[1]))
print(adj)


def dfs(node,adj,visited,pathvis,check):
    visited[node] = 1
    pathvis[node] = 1
    check[node] = 0
    for i in adj[node]:
        if visited[i] != 1 :
            if dfs(i,adj,visited,pathvis,check) == True:
                check[node] = 0
                return True 
        elif visited[i] == 1 and pathvis[i] == 1:
            check[node] = 0
            return True 
    pathvis[node] = 0
    check[node] = 1
    return False




visited = [0]*(n+1)
pathvis = [0]*(n+1)
safe = [0]*(n+1)
for i in range(n):
    if visited[i] != 1:
        dfs(i,adj,visited,pathvis,safe)
print("All Safe Nodes in the Graph : ",end = " ")
for i in range(len(safe)):
    if safe[i] == 1:
        print(i,end = " ")
print()