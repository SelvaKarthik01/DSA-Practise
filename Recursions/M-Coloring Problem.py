"""
Docstring for Recursions.M-Coloring Problem

Given an edges of graph and a number m, the your task is to check it is possible to color the given graph with at most m colors such that no two adjacent vertices of the graph are colored with the same color.

Examples

Input: V = 4, edges[][] = [[0, 1], [0, 2], [0,3], [1, 3], [2, 3]], m = 3
Output: true
Explanation: Structure allows enough separation between connected vertices, so using 3 colors is sufficient to ensure no two adjacent vertices share the same color—hence, the answer is true

M-Coloring-Problem-2
 
Input:  V = 5, edges[][] = [[0, 1], [0, 2], [0, 3], [1, 2], [1, 4], [2, 3], [2, 4], [3, 4]], m = 3
Output: true
Explanation: In this graph, the vertices are highly interconnected, especially vertex 2, which connects to four others. With only 3 colors, it's impossible to assign c
"""

n = int(input("Enter the Number of Vertices : "))
#edges = eval(input("Enter the Edges : "))
edges = [[0, 1], [0, 2], [0,3], [1, 3], [2, 3]]
m = int(input("Enter the Number of Colors : "))
d = {}
for i in range(n):
    d[i] = -1
    
def isSafe(i,edges,color,d):
    for u,v in edges:
        if u == i and d[v] == color:
            return False 
        if v==i and d[u] == color:
            return False
    return True 
def recursion(n,i,edges,m,d):
    if i == n:
        return True

    for color in range(m):
        if isSafe(i,edges,color,d):
            d[i] = color
            if(recursion(n,i+1,edges,m,d)):
                return True
            d[i]=-1
    return False

    
print(recursion(n,0,edges,m,d))
            
