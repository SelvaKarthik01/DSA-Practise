n = int(input("Enter the No. of Stations : "))
m = int(input("Enter the No. of Edges : "))
from collections import defaultdict,deque 
adj = defaultdict(set)

for j in range(m):
    s = input("Enter the Edge : ")
    s = s.split()
    weight = int(input("Enter the Distance : "))
    adj[int(s[0])].add((weight,int(s[1])))
print(adj)
Queue = deque()
src = int(input("Enter the Source Node : "))
dest = int(input("Enter the Destination Node : "))
k = int(input("Enter the Minimum Number of Stops : "))
distance = [float("inf")]*n 
distance[src] = 0 
Queue.append((0,src,0))
while(len(Queue) != 0):
    steps,node,dist = Queue.popleft()
    if steps > k :
        continue
    else: 
        for j,i in adj[node]:
            if distance[node] + j < distance[i] and steps <= k:
                distance[i] = distance[node] + j
                Queue.append((steps+1,i,distance[i]))
if distance[dest] != float("inf"):
    print("Shortest Path from Source Airport ",src," to Destination Airport ",dest," is : ",distance[dest])
else:
    print("You Cannot Reach the Destination Airport ",dest," from Source ",src," !!")
    
