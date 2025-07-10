L = eval(input("Enter the List : "))
index = -1 
for i in range(len(L)-2,-1,-1):
    if L[i] < L[i+1]:
        index = i 
        break
if index == -1 :
    L.reverse()
    print(L)
else:
    max = L[index]
    for i in range(len(L)-1,index,-1):
        if L[i] > L[index]:
            L[i],L[index] = L[index],L[i]
            break 
    left = L[:index+1]
    right = L[index+1:]
    right.reverse()
    left.extend(right)
    print(left)
 
    
    