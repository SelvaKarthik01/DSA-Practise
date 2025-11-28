L = eval(input("Enter the list : "))
k = int(input("Enter the Sum : "))
d = {}
d[0] = 1
sum=0
count = 0
for i in range(len(L)):
    sum += L[i]
    if sum - k in d:
        count += 1
    d[sum-k] = 1 
print(count)
    