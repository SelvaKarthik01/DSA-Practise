L =eval(input("Enter the List : "))
k = int(input("Enter the Sum : "))

d = {}
sum = 0 
len1 = 0 
for i in range(len(L)):
    sum += L[i]
    if sum == k:
        len = i +1
    rem = sum - k
    if rem in d:
        len1 = max(len1,i-d[rem])
    d[sum] = i
print(len1)
# Another Greedy Approach Solution 

i = 0 
j = 1
len1 = 0
sum =L[i]
while(j < len(L)):
    sum += L[j]
    if sum < k:
        j += 1
    elif sum == k :
        len1 = max(len1,j-i+1)
        j += 1
    elif sum > k :
        sum -= L[i]
        i += 1
        j += 1
print(len1)
        
        