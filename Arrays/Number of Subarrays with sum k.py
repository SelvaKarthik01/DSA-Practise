"""
Docstring for Arrays.Number of Subarrays with sum k

Time Complexity : O(n)
Space Complexity : O(n)

"""

L = eval(input("Enter the List : "))
k = int(input("Enter the Target Sum : "))
ans = 0 
d = {}
sum = 0
for i in range(len(L)):
    sum += L[i]
    if sum == k:
        ans += 1
    if sum - k in d:
        ans += d[sum-k]
    d[sum] = d.get(sum,0) + 1
print(ans)
    