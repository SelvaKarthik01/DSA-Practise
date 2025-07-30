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