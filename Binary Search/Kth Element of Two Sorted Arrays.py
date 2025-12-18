"""
Docstring for Binary Search.Kth Element of Two Sorted Arrays

Time Complexity : O(log(min(L1,L2)))
Space Complexity : O(1)

"""
def Binary_Search(L1,L2,k):
    if len(L1) > len(L2):
        L1,L2 = L2,L1
    low = max(0,k-len(L2))
    high = min(k,len(L1))
    while(low <= high):
        mid1 = low + (high-low)//2
        mid2 = k - mid1 
        left1,left2 = float("-inf"),float("-inf")
        right1,right2 = float("inf"),float("inf")
        if mid1-1 >= 0:
            left1 = L1[mid1-1]
        if mid2-1 >= 0:
            left2 = L2[mid2-1]
        if mid1 < len(L1):
            right1 = L1[mid1]
        if mid2 < len(L2):
            right2 = L2[mid2]
        if left1 <= right2 and left2 <= right1:
            return max(left1,left2)
        elif left1 > right2:
            high = mid1 - 1
        else:
            low = mid1 + 1
            
L1 = eval(input("Enter the First Sorted List : "))
L2 = eval(input("Enter the Second Sorted List : "))
k = int(input("Enter the Value for K : "))
print(Binary_Search(L1,L2,k))
