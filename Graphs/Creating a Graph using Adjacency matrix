print("Undirected graph")
n = int(input("Enter the Number of Nodes : "))
m = int(input("Enter the Number of Edges : "))
adj = []
for i in range(n+1):
    temp = []
    for j in range(n+1):
        temp.append(0)
    adj.append(temp)
for i in range(1,n+1):
    for j in range(1,n+1):
        print(adj[i][j],end = " ")
    print() 
for i in range(m):
    s = input("Enter the Edges between vertices : ")
    adj[int(s[0])][int(s[2])] = 1
    adj[int(s[2])][int(s[0])] = 1
for i in range(1,n+1):
    for j in range(1,n+1):
        print(adj[i][j],end = " ")
    print() 

    