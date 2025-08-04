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
color = []
for i in range(n+1):
    color.append(-1)
def dfs(start,col,color,adj):
    color[start] = col 
    for i in adj[start]:
        if color[i] == -1 and col == 0:
            if (dfs(i,1,color,adj)== False):
                return False
        elif color[i] == -1 and col == 1:
            if(dfs(i,0,color,adj) == False):
                return False
        elif color[i] != -1 and color[i] == col:
            return False 
    return True

for i in range(1,n+1):
    if color[i] == -1:
        if dfs(i,0,color,adj) == False:
            print("Not a Bipartite Graph !!")
            break
else:
    print("It is a Bipartite Graph !!")
    