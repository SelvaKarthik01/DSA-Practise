from collections import defaultdict , deque
n = int(input("Enter the Number of Nodes : "))
m = int(input("Enter the No. of Edges : "))
adj = defaultdict(set)
for i in range(m):
    s = input("Enter the Edges : ")
    s= s.split()
    adj[int(s[0])].add(int(s[1]))
    adj[int(s[1])].add(int(s[0]))
print(adj)
visited = [0] * (n+1)

def bfs(start,visited,adj):
    Queue = deque()
    Queue.append([start,0])
    visited[start] = 1
    while(len(Queue) != 0):
        ans = Queue.popleft()
        start = ans[0]
        parent = ans[1]
        for i in adj[start]:
            if visited[i] != 1:
                visited[i] = 1
                Queue.append([i,start])
            elif parent != i:
                return True 
    return False 

for i in range(1,n+1):
    if visited[i] != 1:
        if bfs(i,visited,adj):
            print("Cycle Detected")
            break
else:
    print("Cycle Not Detected")
        
            