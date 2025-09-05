n = int(input("Enter the Number of Nodes : "))
m = int(input("Enter the Number of Edges : "))
power_edges = eval(input("Enter the Power Nodes : "))
from collections import defaultdict,deque
adj = defaultdict(set)
for i in range(m):
    s = input("Enter the Edges").split()
    adj[int(s[0])].add(int(s[1]))
    adj[int(s[1])].add(int(s[0]))
print(adj)
Queue = deque()
visited = set()
Queue.append((1,0))
while(len(Queue) != 0):
    node,power = Queue.popleft()
    for i in adj[node]:
        if i not in visited: 
            visited.add(i)
            if i == n:
                print(power + 1)
            else:
                if i in power_edges:
                    Queue.append((i,0))
                else:
                    Queue.append((i,power+1))
print(-1)
            
                