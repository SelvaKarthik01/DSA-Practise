# You can move only Down and Right 
n = int(input("Enter the Maze Dimension : "))
visited = [[0 for _ in range(n)] for _ in range(n)]
def recursion(n,row,col,path,visited,ans):
    if row ==n-1 and col == n-1:
        ans.append(list(path))
        return 
    drow = [0,+1]
    dcol = [+1,0]
    for i in range(len(drow)):
        nrow = row + drow[i]
        ncol = col + dcol[i]
        if nrow >= 0 and nrow < n and ncol >= 0 and ncol < n and visited[nrow][ncol] == 0:
            visited[nrow][ncol] = 1
            path.append((nrow,ncol))
            recursion(n,nrow,ncol,path,visited,ans)
            path.pop()
            visited[nrow][ncol] = 0 
    return 
ans = []
visited[0][0] = 1
path = []
path.append((0,0))
recursion(n,0,0,path,visited,ans)
print(ans)
    