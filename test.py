def Binary_Search(L):
    low = 0 
    high = len(L)-1
    ans = float("inf")
    index = -1
    while(low<= high):
        mid = low + (high-low)//2
        if L[low] <= L[mid]:
            if L[low] < ans:
                ans = L[low]
                index = low 
            low = mid + 1
        else:
            if L[mid] < ans:
                ans = L[mid]
                index = mid 
            high = mid - 1
    return high
            
L = eval(input("Enter the List : "))
print(Binary_Search(L))
