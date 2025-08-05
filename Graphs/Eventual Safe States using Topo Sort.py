from collections import deque,defaultdict
n = int(input("Enter the Total No. of Nodes : "))
m = int(input("Enter the Total No. of Edges : "))
adj = defaultdict(set)
indegree=[0]*(n)
for i in range(m):
    s = input("Enter the Edge : ")
    s = s.split()
    adj[int(s[0])].add(int(s[1]))
    
print(adj)
Queue = deque()
new_adj = defaultdict(set)
for i in range(n):
    for j in adj[i]:
        new_adj[j].add(i)
print(new_adj)
for i in range(len(indegree)):
    if indegree[i] == 0 :
        Queue.append(i)
result = []
while(len(Queue)!= 0):
    node = Queue.popleft()
    result.append(node)
    for i in new_adj[node]:
        indegree[i] -= 1
        if indegree[i] == 0 :
            Queue.append(i)
result.sort()
print("Safe States : ",end = " ")
for i in result:
    print(i,end = " ")

