"""
Docstring for Arrays.Count No. of Subarrays with Sum K

Another Appraoch is to create all possible subarrays and find those subarrays whose element sum is k 
TC-> O(n^2) -> n^2 for subarray with element i
SC -> O(1) 


Time Complexity : O(n)
Space Complexity : O(n) for the seen hashmap 

"""
L = eval(input("Enter the list : "))
k = int(input("Enter the Sum : "))
d = {}
d[0] = 1
sum=0
count = 0
for i in range(len(L)):
    sum += L[i]
    if sum - k in d:
        count += 1
    d[sum-k] = 1 
print(count)
    