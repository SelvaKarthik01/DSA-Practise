from collections import defaultdict, deque
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
def bfs(start,color,adj):
    Queue = deque()
    color[start] = 0
    Queue.append(start)
    while(len(Queue) != 0):
        ans = Queue.popleft()
        col = color[ans]
        for i in adj[ans]:
            if color[i] != -1 and col == color[i]:
                return False 
            elif color[i] == -1 and col == 0:
                color[i] = 1
                Queue.append(i)
            elif color[i] == -1 and col == 1:
                color[i] = 0
                Queue.append(i)
    return True 
start = int(input("Enter the Start Node : "))
if bfs(start,color,adj):
    print("It is a Bipartite Graph")
else:
    print("Not a Bipartite Graph") 
    