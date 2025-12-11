"""
Docstring for Arrays.Max Subarray Sum

One Approach find out all the subarrays and then find the max sum of the subarray 
TC-> O(n^2) -> Generating all Subarrays + O(n) to find their sum 
SC-> O(1)

Kadane's Algorithm

Time Complexity : O(n)
Space Complexity : O(n)

"""

L = eval(input("Enter the List : "))
sum = 0 
max_sum = 0
for i in range(len(L)):
    sum += L[i]
    if sum < 0: # No use in carrying a sum lesser 
        sum = 0 
    max_sum = max(max_sum,sum)
print(max_sum)


""" 
If negative elements are present:

class Solution(object):
    def maxSubArray(self, nums):
        sum = 0 
        max_sum = float("-inf")
        for i in range(len(nums)):
            sum = max(nums[i],sum+nums[i])
            max_sum = max(sum,max_sum)
        return max_sum
        
"""
