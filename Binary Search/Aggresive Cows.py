"""
Docstring for Binary Search.Aggresive Cows

This is an Example of min(max) or max(min) in binary Search 

Time Complexity : O(nlogn) + O(nlogn) -> O(nlogn)
Space Complexity : O(1)

"""
def IsPossible(L,n,dist):
    last_placed = L[0] 
    n = n - 1
    for i in range(1,len(L)):
        if L[i] - last_placed >= dist:
            n -= 1
            last_placed = L[i]
    if n <= 0:
        return True
    else:
        return False
def Binary_Search(L,n):
    low = 1
    high = max(L)-min(L)
    while(low<=high):
        mid = low + (high-low)//2
        if IsPossible(L,n,mid):
            low = mid + 1
        else:
            high = mid - 1
    return high
L = eval(input("Enter the List : "))
n = int(input("Enter the No. of Cows : "))
L.sort()
print(Binary_Search(L,n))