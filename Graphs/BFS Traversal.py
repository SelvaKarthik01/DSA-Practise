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
start = int(input("Enter the Starting node for BFS : "))
from collections import deque 
Queue = deque() 
visited = []
for i in range(n+1):
    visited.append(0) 
visited[0] = 1
visited[start] = 1
Queue.append(start)
print("BFS -> ",end =  " ")
while(len(Queue) != 0):
    for i in adj[Queue[0]]:
        if visited[i] != 1:
            visited[i] = 1
            Queue.append(i)
    print(Queue.popleft(),end =  " ")
    
    
        