"""
Docstring for Binary Search.Largest Subarray Sum after k Splits

Time Complexity : O(nlogn)
Space Complexity : O(1)

"""
def isSplit(L,k,max_sum):
    sum = 0 
    split = 1 
    for i in range(len(L)):
        if sum + L[i] <= max_sum:
            sum += L[i]
        else:
            split += 1
            sum = L[i]
    if split <= k :
        return True 
    elif split > k :
        return False 
        

def Binary_Search(L,k):
    low = max(L)
    high = sum(L)
    while(low <= high):
        mid = low + (high-low)//2
        if isSplit(L,k,mid):
            ans = mid 
            high = mid - 1
        else:
            low = mid + 1
    return ans 
            
L = eval(input("Enter the List : "))
k = int(input("Enter the Splits : "))
print(Binary_Search(L,k))
