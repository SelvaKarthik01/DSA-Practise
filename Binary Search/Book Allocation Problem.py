"""
Docstring for Binary Search.Book Allocation Problem

Given an array nums of n integers, where nums[i] represents the number of pages in the i-th book, and an integer m representing the number of students, allocate all the books to the students so that each student gets at least one book, each book is allocated to only one student, and the allocation is contiguous.



Allocate the books to m students in such a way that the maximum number of pages assigned to a student is minimized. If the allocation of books is not possible, return -1.


Example 1

Input: nums = [12, 34, 67, 90], m=2

Output: 113

Explanation: The allocation of books will be 12, 34, 67 | 90. One student will get the first 3 books and the other will get the last one.

Example 2

Input: nums = [25, 46, 28, 49, 24], m=4

Output: 71

Explanation: The allocation of books will be 25, 46 | 28 | 49 | 24.

Time Complexity : O(nlogn)
Space Complexity : O(1)

"""

def IsAllocation(L,m,pages):
    sum = L[0]
    for i in range(1,len(L)):
        if sum + L[i] <= pages:
            sum += L[i]
        else:
            m-= 1
            sum = L[i]
    m -= 1
    if m >= 0:
        return True
    elif m < 0:
        return False 
     

def Binary_Search(L,m):
    if len(L) < m:
        return -1
    low = max(L)
    high = sum(L)
  
    ans = -1
    while(low <= high):
        mid = low + (high-low)//2
        if IsAllocation(L,m,mid):
            ans = mid 
            high = mid - 1
        else:
            low = mid + 1
    return ans
L = eval(input("Enter the Books : "))
m = int(input("Enter the No. of Students : "))
print(Binary_Search(L,m))