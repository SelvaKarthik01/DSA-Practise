"""
Docstring for Arrays.Union of two sorted lists

Another approach is to go through both the elements and store the elements in the set or hashmap 
Storing Elements v-> O(n)
Removing and Storing in ans array - >O(n)
Total -> O(2n) -> O(n)

Time Complexity : O(n)
Space Complexity : O(1) -> Auxiliary Space O(n) for saving the answer array 

"""


L1 = eval(input("Enter the First List : "))
L2 = eval(input("Enter the Second List : "))
i = 0 
j = 0 
ans = []
last_updated = float("inf")
while(i < len(L1) and j < len(L2)):
    if L1[i] <= L2[j]:
        if L1[i] != last_updated:
            ans.append(L1[i])
            last_updated = L1[i]
        i += 1 
        
    elif L2[j] < L1[i]:
        if last_updated != L2[j]:
            ans.append(L2[j])
            last_updated = L2[j]
        j += 1
        
while(i < len(L1)):
    if L1[i] != last_updated: 
        ans.append(L1[i])
        last_updated = L1[i]
    i += 1
    
while( j < len(L2)):
    if last_updated != L2[j]:
        ans.append(L2[j])
        last_updated = L2[j]
    j +=1 
print(ans)
        
        