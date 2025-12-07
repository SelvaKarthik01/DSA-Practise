#L = eval(input("Enter the Grid of Array : "))
L = [['a','x','a'],['x','b','x'],['a','x','a']]
n = len(L)
visited = [[0 for _ in range(n)]for _ in range(n)]
visited[0][0] = 1
visited[len(L)-1][len(L)-1] = 1

    
def recursion(L,row,col,row1,col1,path,visited,ans):
    if row == row1 and col == col1:
        final_path = list(path[:len(path)])
        for i in range(len(path)-2,-1,-1):
            final_path.append(path[i])
        if len(ans) == 0 or len(final_path) == len(ans[0]):
            ans.append("".join(final_path))
        if len(path) > len(ans[0]):
            ans = []
            ans.append("".join(final_path))
        return 
    drow = [0,1]
    dcol = [1,0]
    drow1 = [0,-1]
    dcol1 = [-1,0]
    for i in range(len(drow)):
        nrow = row + drow[i]
        ncol = col + dcol[i]
        for j in range(len(drow1)):
            nrow1 = row1 + drow1[j]
            ncol1 = col1 + dcol1[j]
            if nrow < len(L) and ncol < len(L) and nrow1 >= 0 and ncol1 >= 0 and visited[nrow][ncol]==0 and visited[nrow1][ncol1]==0 and L[nrow][ncol] == L[nrow1][ncol1]:
                visited[nrow][ncol] = 1
                visited[nrow1][ncol1] = 1
                path.append(L[nrow][ncol])
                recursion(L,nrow,ncol,nrow1,ncol1,path,visited,ans)   
                path.pop()
                visited[nrow][ncol] =0
                visited[nrow1][ncol1] = 0
    return 

if L[0][0] == L[n-1][n-1]:
    path = []
    path.append(L[0][0])
    ans = []
    recursion(L,0,0,len(L)-1,len(L)-1,path,visited,ans)
    print("All Possible Paths : ",ans)
    print("Unique Paths : ",set(ans))
else:
    print("")

                     
    
    