from collections import defaultdict,deque
n = int(input("Enter the Total Number of tasks : "))
p = int(input("Enter the No. of Prerequistes : "))
adj = defaultdict(set)
indegree = [0]*(n+1)
for i in range(p):
    s = input("Enter the Prerequisite : ")
    s = s.split()
    adj[int(s[0])].add(int(s[1]))
    indegree[int(s[1])]+=1 
print(adj)
Queue = deque()
for i in range(1,len(indegree)):
    if indegree[i] == 0 :
        Queue.append(i)
result = []
while(len(Queue) != 0):
    node = Queue.popleft()
    result.append(node)
    for i in adj[node]:
        indegree[i] -= 1
        if indegree[i] == 0 :
            Queue.append(i)
if len(result) == n:
    print("Yes Task Completion is Possible !!")
else:
    print("No task Completion is not Possible !!")