"""
Docstring for Arrays.Three Sum

Another Approarch is to find the all possible triplets and find the triplets with sum as target 

TC-> O(N^3) 
SC -> O(Number of triplets)

ANother Approach is using the fact that 
arr[i] + arr[j] + arr[k] = target 
arr[k] = target - arr[i] - arr[j]

We only loop thourgh i and j and find the target-arr[i]-arr[j] present in hashmap 
TC-> O(n^2) only for i and j 
SC -> O(n)

Time Complexity: O(nlogn) for sorting + O(n^2) for keeping i constant and moving j and k 
                 Total -> O(nlogn + n^2) -> O(n^2)
Space Compleixty : O(1) -> Auxiliary Space O(Number of triplets)

This is very similar to the Two Sum but here we are keeping i as constant and perfroming the same 
"""
L = eval(input("Enter the List : "))
L.sort()
target = int(input("Enter the Target Element : "))
i = 0 
ans = []
while(i < len(L)):
    j = i +1 
    k = len(L)-1
    while(k >= 0 and j < len(L) and j < k):
        if L[i] + L[j] + L[k] < target:
            j += 1
        elif L[i] + L[j] + L[k] > target:
            k -= 1 
        else:
            if L[i] + L[j] + L[k] == target:
                ans.append([L[i],L[j],L[k]])
                temp = L[j]
                while(j < k and L[j] == temp):
                    j += 1
                temp = L[k]
                while(j < k and L[k] == temp):
                    k -= 1
    temp = L[i]
    while(i < len(L) and L[i]==temp):
        i += 1
print(ans)
                
            