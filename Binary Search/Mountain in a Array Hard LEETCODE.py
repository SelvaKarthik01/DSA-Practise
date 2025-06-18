""" 
1095. Find in Mountain Array
Hard
Topics
premium lock icon
Companies
Hint
(This problem is an interactive problem.)

You may recall that an array arr is a mountain array if and only if:

arr.length >= 3
There exists some i with 0 < i < arr.length - 1 such that:
arr[0] < arr[1] < ... < arr[i - 1] < arr[i]
arr[i] > arr[i + 1] > ... > arr[arr.length - 1]
Given a mountain array mountainArr, return the minimum index such that mountainArr.get(index) == target. If such an index does not exist, return -1.

You cannot access the mountain array directly. You may only access the array using a MountainArray interface:

MountainArray.get(k) returns the element of the array at index k (0-indexed).
MountainArray.length() returns the length of the array.
Submissions making more than 100 calls to MountainArray.get will be judged Wrong Answer. Also, any solutions that attempt to circumvent the judge will result in disqualification.

 

Example 1:

Input: mountainArr = [1,2,3,4,5,3,1], target = 3
Output: 2
Explanation: 3 exists in the array, at index=2 and index=5. Return the minimum index, which is 2.
Example 2:

Input: mountainArr = [0,1,2,4,2,1], target = 3
Output: -1
Explanation: 3 does not exist in the array, so we return -1.
"""
L = eval(input("Enter the List : "))
target = int(input("Enter the target element : "))

def peak_element(L):
    start = 0
    end = len(L) - 1
    while(start < end):
        mid = start + (end - start)//2
        if L[mid] > L[mid + 1]:
            end = mid
        else:
            start = mid + 1
    return start 

def binary_search_asc(L,target,start=0,end=len(L)-1):
    while(start <= end):
        mid = start + (end - start)//2
        if L[mid] == target:
            return mid
        if L[mid] > target :
            end = mid -1
        if L[mid] < target:
            start = mid + 1
    return -1
def binary_search_desc(L,target,start=0,end=len(L)-1):
    while(start <= end):
        mid = start + (end - start)//2
        if L[mid] == target:
            return mid
        if L[mid] > target :
            start = mid + 1
        if L[mid] < target:
            end = mid - 1
    return -1
peak = peak_element(L)
if binary_search_asc(L,target,0,peak) == -1:
    print(binary_search_desc(L,target,peak+1))
else:
    print(binary_search_asc(L,target,0,peak))
    
        

    
    