"""
Docstring for Binary Search.kth Missing Number

[2,3,4,7,11]
[1,2,3,4,5] -. Ideally this mus have been the array 
[1,1,1,3,6] -> Number os missing by subracting the guven - ideal 
we find in which range the k lies in get the floor value of it and check how many number should we go by k - floor 
Add this to L[high]

Time Compleixty : O(n)+O(logn) -> O(n)
Space Complexity : O(1)

"""
def Binary_Search(L,k):
    missing = []
    for i in range(1,len(L)+1):
        missing.append(L[i-1]-i)
    low = 0 
    high = len(missing)-1
    while(low <= high):
        mid = low + (high-low)//2
        if missing[mid] < k:
            low = mid + 1
        else:
            high = mid - 1
    if high ==-1:
        return k
    number_missing = k-missing[high]
    return L[high] + number_missing  
    
L = eval(input("Enter the List : "))
k = int(input("Enter the Value of k : "))
print(Binary_Search(L,k))
