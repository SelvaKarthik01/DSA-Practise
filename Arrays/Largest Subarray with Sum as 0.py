"""
Docstring for Arrays.Largest Subarray with Sum as 0

Time Complexity : O(n)
Space Complexity : O(n)
"""
L = eval(input("Enter the List : "))
sum = 0 
d = {}
max_len = -1
for i in range(len(L)):
    sum += L[i]
    if sum == 0:
        max_len = max(max_len,i+1)
    elif sum in d:
        max_len = max(max_len,i-d[sum])
    if sum not in d:
        d[sum] = i 
print(max_len)        