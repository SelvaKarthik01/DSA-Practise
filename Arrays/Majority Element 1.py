"""
Docstring for Arrays.Majority Element 1

=> Element Present more than N/2 times 

One Approach is coutn each element using two loops and check if any any element is greater or not 
TC -> O(n^2) -. For two loops 
SC -> O(1) 

Another approach is using a Counter that is count each and every element and store in hashmap and check every element

class Solution(object):
    def majorityElement(self, nums):
        d = {}
        from collections import Counter 
        count = Counter(nums)
        for i in count:
            if count[i] > len(nums)//2:
                return i 

TC -> O(n)-> for storing in hashmap + O(n)-> for finding the highest count 
SC -> O(n)

Moore's Voting Algorithm:
O(n) -> For finding the max dominated element in the array 
O(n) -> To check the correctness of the algorithm if its >N/2


Time Complexity : O(n) + O(n) for checking if its correct -> O(2n) 
Space Complexity : O(1)

"""

L = eval(input("Enter the List : "))

el = L[0]
count = 0 
for i in range(len(L)):
    if count == 0:
        el = L[i]
        count = 1
    elif L[i] == el:
        count += 1 
    else:
        count -= 1
count = 0
for i in range(len(L)):
    if L[i] == el:
        count += 1
if count > len(L)//2:
    print(el)
else:
    print("Not Found!!")
