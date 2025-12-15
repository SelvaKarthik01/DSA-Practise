"""
Docstring for Binary Search.Minimum Number of Days to make M bouquets\

Time Complexity : O(n)*O(logn) -> O(nlogn)
Space Complexity : O(1)

"""

def Bouquets(L,n,flowers): 
    bouquets = 0
    count = 0
    for i in range(len(L)):
        if L[i] <= n:
            count += 1
        else:
            bouquets += count//flowers
            count = 1
    bouquets += count//flowers
    return bouquets
        

def Binary_Search(L,n,m):
    
    if len(L) < m*n:
        return -1
    
    low = min(L)
    high = max(L)
    while(low <= high):
        mid = low + (high-low)//2
        if Bouquets(L,mid,m) >= n:
            ans = mid 
            high = mid - 1
        else:
            low = mid + 1
    return low

L = eval(input("Enter the Flowers : "))
n = int(input("Enter the Number of Bouqeuts : "))
m = int(input("Enter the Flowers : "))
print(Binary_Search(L,n,m))
