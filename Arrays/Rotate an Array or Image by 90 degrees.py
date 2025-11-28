n = int(input("Enter the Rows of the Matrix : "))
m = int(input("Enter the Columns in the Matrix : "))
L = [[0 for i in range(m)] for i in range(n)]
# TO find the transpose of the mAtrix 

for i in range(n):
    for j in range(m):
        print("L[",i,"][",j,"]: ",end = "")
        L[i][j] = int(input())
for i in range(n-1):
    for j in range(i+1,n):
        L[i][j],L[j][i] = L[j][i],L[i][j]
for i in range(n):
    print(L[i])
    L[i][::]= reversed(L[i][::])
print(L)
