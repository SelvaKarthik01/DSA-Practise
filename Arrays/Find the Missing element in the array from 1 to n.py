"""
Docstring for Arrays.Find the Missing element in the array from 1 to n

Another approach is loop from 1 to n and linear search each element
TC-> O(n^2) for every element Linear Search 
SC -> O(1) 
Another Approach is using Bitwise Xor Operations 
Create a array from 1 to n find the xor 
Find the xor of the given array 
Xor both the answers to find the missing number 

TC -> O(n) if we dont know the formula else O(1)
SC -> O(n) if we dont know the formula else O(1)

Xor Formulas: 
Xor % 4 == 0 : a
Xor % 4 == 1 : 1
Xor % 4 == 2: a + 1
Xor % 4 == 3 : 0

Another Solution:
With explicitly using a loop using the same loop for xor calculation

class Solution(object):
    def missingNumber(self, nums):
        xor1,xor2 =0,0
        for i in range(len(nums)):
            xor1 ^= nums[i]
            xor2 ^= (i+1)
        return xor1^xor2
TC -> O(n)
SC -> O(1)


Time Complexity: O(n) -> for finding the sum of all elements in given array 
Space Complexity: O(1) -> No Extra spaces taken 
"""


L = eval(input("Enter the List : "))
n = int(input("Enter the value for N : "))
expected_sum = (n*(n+1))//2
actual_sum = sum(L)
missing_num = expected_sum - actual_sum
print(missing_num)