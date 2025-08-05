n = int(input("Enter the No. of Nodes : "))
m = int(input("Enter the No. of Edges : "))


from collections import defaultdict,deque
adj = defaultdict(set)
for i in range(m):
    s = input("Enter the Edges : ")
    s = s.split()
    adj[int(s[0])].add(int(s[1]))
    adj[int(s[1])].add(int(s[0]))
print(adj)

Queue = deque()
distance = [float("inf")]*n

src = int(input("Enter the Source Node : "))
distance[src] = 0
Queue.append((src,0))
while(len(Queue) != 0):
    node,weight = Queue.popleft()
    for i in adj[node]:
        if distance[node] + 1 < distance[i]:
            distance[i] = distance[node] + 1
            Queue.append((i,distance[i]))
for i in distance:
    if i == float("inf"):
        print("Shortest Path not Possible !!")
else:
    print("Shortest Paths from the Source Node ",src," : ",end = " ")
    for i in range(len(distance)):
        print(distance[i],end = " ")
