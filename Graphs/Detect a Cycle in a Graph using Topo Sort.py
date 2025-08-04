n = int(input("Enter the Number of Nodes : "))
m = int(input("Enter the No. of Edges : "))
from collections import defaultdict,deque
adj = defaultdict(set)
Queue = deque()
indegree = [0]*(n+1)
for i in range(m):
    s = input("Enter the Edge : ")
    s = s.split()
    adj[int(s[0])].add(int(s[1]))
    indegree[int(s[1])] += 1
print(adj)
result = []
for i in range(1,len(indegree)):
    if indegree[i] == 0 :
        Queue.append(i)
while(len(Queue) != 0):
    node = Queue.popleft()
    result.append(node)
    for i in adj[node]:
        indegree[i] -= 1
        if indegree[i] == 0 :
            Queue.append(i)
if len(result) == n :
    print("No Cycle Detected in a Graph !!")
else:
    print("Cycle Detected in a Graph !!")
