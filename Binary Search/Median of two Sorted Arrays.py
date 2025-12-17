"""
Docstring for Binary Search.Median of two Sorted Arrays

Time Complexity : O(log(min(n,m)))
Space Complexity : O(1)
"""
def Median(L1,L2):
    no_elements = (len(L1)+len(L2))//2
    low = 0 
    high = min(len(L1),len(L2))
    if len(L1) > len(L2):
        small = L2 
        big = L1 
    else:
        small = L1 
        big = L2
    while(low<= high):
        mid1 = low + (high-low)//2
        mid2 = no_elements - mid1
        if mid1-1 < 0:
            left1 = float("-inf")
        else:
            left1 = small[mid1-1]
        if mid2-1 < 0:
            left2 = float("-inf")
        else:
            left2 = big[mid2-1]
        if mid1 == len(small):
            right1 = float("inf")
        else:
            right1 = small[mid1]
        if mid2 == len(big):
            right2 = float("inf")
        else:
            right2 = big[mid2]
        if left1 < right2 and left2 < right1:
            if (len(L1)+len(L2))%2 == 0:
                return (max(left1,left2) + min(right1,right2))/2
            else:
                return max(max(left1,left2),min(right1,right2))
        elif left1 > right2:
            high = mid1 -1
        else:
            low = mid1 + 1
    return -1
        
        
L1 = eval(input("Enter the First Sorted List : "))
L2 = eval(input("Enter the Second Sorted List : "))
print(Median(L1,L2))
