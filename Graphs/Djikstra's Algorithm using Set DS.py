n = int(input("Enter the No. of Nodes : "))
m = int(input("Enter the No. of Edges : "))
from collections import defaultdict 
adj = defaultdict(set)
for i in range(m):
    s = input("Enter the Edges : ")
    weight = int(input("Enter the Weight of the Edge : "))
    s = s.split()
    adj[int(s[0])].add((weight,int(s[1])))
    adj[int(s[1])].add((weight,int(s[0])))
print(adj)
distance = [float("inf")]*n
src = int(input("Enter the Source Node : "))
distance[src] = 0
Queue = set()
Queue.add((0,src))
while(len(Queue) != 0):
    print(Queue)
    print(min(Queue))
    temp = min(Queue)
    node = temp[1]
    Queue.remove(temp)
    for i,j in adj[node]:
        if distance[node] + i < distance[j]:
            distance[j] = distance[node] + i 
            Queue.add((distance[j],j))
print("Shortest Path to all the Nodes from the Source Node : ",src," : ")
for i in range(len(distance)):
    print(i," --> ",distance[i])