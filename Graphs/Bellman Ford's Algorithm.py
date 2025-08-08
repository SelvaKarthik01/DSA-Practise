n = int(input("Enter the No. of Nodes : "))
edges = eval(input("Enter the Edges and Weightys in a List : "))
distance = [float("inf")]*n 
src = int(input("Enter the Source Node : "))
distance[src] = 0
found = False
for i in range(n+1):
    for j in edges:
        u = j[0]
        v = j[1]
        wt = j[2]
        if i == n and distance[v] != float("inf") and distance[u] + wt == distance[v]:
            continue 
        elif i == n and distance[v] != float("inf") and distance[u] + wt < distance[v]:
            print("Negative Weight Cycle Encountered !!")
            found = True 
            break
        if distance[v] != float("inf") and distance[u] + wt < distance[v]:
            distance[v] = distance[u] + wt 
    if found == True:
        break
else:
    for i in range(len(distance)):
        print(i," --> ",distance[i])
