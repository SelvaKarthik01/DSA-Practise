"""
Docstring for Arrays.Length of the Longest Subarray of Sum k

Another Approach is generate all the possible subarray and check each subarray if its sum == k 
TC -> O(n^2) -> for generating subarrays 
      k*O(n) -> for finding the sum of each subarray if we have k subarray
      Total -> O(n^2) + O(n^2) -> O(2n^2) -> O(n^2)
SC -> O(n^2) for storing all possible subarrays 

Time Complexity : O(n)
Space Complexity : O(1)

"""

# Prefix Sum Algorithm applicable for +ve, -ve and 0 as elements in the array 
L = eval(input("Enter the List : "))
k = int(input("Enter the target Sum : "))
d = {}
max_len = -1
sum = 0
for i in range(len(L)):
    sum += L[i]
    if sum == k :  # Present at the starting itself 
        max_len = max(max_len,i+1) 
    if (sum -k) in d:   # Prefix-Sum 
        max_len = max(max_len,i-d[sum-k]) 
    if sum not in d:
        d[sum] = i 
print(max_len)


# Greedy Algorithm only applicable for +ve and 0 as elements in List 
# Comparitively lesser Time Complexity with lesser whole loops running 
# Time Complexity : O(n)
# Space Compleixty : O(1)
max_len = -1
i = 0
j = 0
curr = 0

while j < len(L):
    curr += L[j]

    while curr > k and i <= j:
        curr -= L[i]
        i += 1

    if curr == k:
        max_len = max(max_len, j - i + 1)

    j += 1

print(max_len)
    