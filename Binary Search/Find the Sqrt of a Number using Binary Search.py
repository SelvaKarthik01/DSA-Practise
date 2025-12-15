"""
Docstring for Binary Search.Find the Sqrt of a Number using Binary Search

Time Complexity : O(logn)
Space Complexity : O(1)
"""

def Binary_Search(n):
    low = 0 
    high = n+1
    ans = -1
    while(low <= high):
        mid = low + (high-low)//2
        if mid*mid <= n:
            ans = mid
            low = mid + 1
        else:
            high = mid -1 
    return ans
n = eval(input("Enter the Number N : "))
print(Binary_Search(n))
