n = int(input("Enter the Number of Cities : "))
m = int(input("Enter the Number of Roads : "))
matrix = [[float("inf")]*n for _ in range(n)]
for i in range(m):
    s = input("Enter the Edge : ")
    s = s.split()
    weight = int(input("Enter the Weight : "))
    matrix[int(s[0])][int(s[1])] = weight
    matrix[int(s[1])][int(s[0])] = weight
for i in range(n):
    matrix[i][i] = 0
for k in range(n):
    for i in range(n):
        for j in range(n):
            matrix[i][j] = min(matrix[i][j],matrix[i][k]+matrix[k][j])
threshold = int(input("Enter the Threshold Distance : "))
result = [[] for _ in range(n)]
min_length = float("inf")
ans = []
for i in range(n):
    for j in range(n):
        if i != j and matrix[i][j] <= threshold:
            result[i].append(j)
    if len(result[i]) < min_length:
        min_length = len(result[i])
        ans=[]
        ans.append(i)
    elif len(result[i]) == min_length:
        ans.append(i)
print(max(ans))

        