L = eval(input("Enter the List : "))
target = int(input("Enter the Target : "))
i = 0 
j = len(L)-1
while(i < j):
    sum = L[i] + L[j]
    if sum > target :
        j -= 1
    elif sum < target:
        i += 1
    elif sum == target:
        ans = [i,j]
        break
print(ans)