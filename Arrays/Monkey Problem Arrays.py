L = eval(input("Enter the List : "))
ans = []

for i in range(len(L)-1):
    count = 0 
    largest = float("-inf")
    for j in range(i+1,len(L)):
        if L[j] > largest and L[j] <= max(L[i],):
            count += 1
            largest = L[j]
    ans.append(count)
ans.append(0)
print(ans)