L = eval(input("Enter the List : "))

ans = []
while(True):
    index = -1 
    n = len(L)
    for i in range(n-2,-1,-1):
        if L[i] < L[i+1]:
            index = i 
            break
    if index == -1 :
        L.reverse()
        ans.append(L)
        break
    for i in range(n-1,index,-1):
        if L[i] > L[index]:
            L[i],L[index] = L[index],L[i]
            break
    left = L[:index+1]
    right = L[index+1:]
    right.reverse()
    left.extend(right)
    ans.append(left)
    L = list(left)
print(ans)