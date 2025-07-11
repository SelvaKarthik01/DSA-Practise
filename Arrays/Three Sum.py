L = eval(input("Enter the List : "))
target = int(input("Enter the Target Sum : "))
L.sort()
ans = []
i = 0
while(i < len(L)):
    prev = L[i]
    j = i +1 
    k = len(L)-1
    while(j < k):
        sum = L[i]+L[j]+L[k]
        if sum == target :
            ans.append([L[i],L[j],L[k]])
            temp = L[j]
            while(j < k and L[j] == temp):
                j += 1
            temp = L[k]
            while(j < k and L[k] == temp):
                k -= 1
        elif sum > target:
            k -= 1
        elif sum < target :
            j += 1
    while(i < len(L) and L[i] == prev):
        i += 1
print(ans)