# Search an Element in a 2D Array where thr rows and colums are sorted  using Binary Search
row = int(input("Enter the Row : "))
col = int(input("Enter the Columns : "))
target = int(input("Enter the Target element : "))
L = []
L1 = []
for i in range(row):
    L1 = []
    for j in range(col):
        L1.append(int(input()))
    L.append(L1)
    
print(L)
r = 0 
c = len(L) - 1
while(r < len(L) and col >= 0):
    if L[r][c] == target:
        
        print(r,c)
        break
    if L[r][c] < target:
        r += 1
    if L[r][c] > target:
        c -= 1
print(-1,-1)
 