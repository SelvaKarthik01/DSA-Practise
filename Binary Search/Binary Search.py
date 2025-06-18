# Binary serach algorithm O(log n)
L = eval(input("Enter the List : "))
L.sort()
n = int(input("Enter the Number to be Searched : "))
def binary_search(L,n):
    start = 0 
    end = len(L)-1
    while(start <= end):
        mid = (start + (end))//2
        if L[mid] == n:
            return mid
            break
        if L[mid] > n :
            end = mid -1
        if L[mid] < n :
            start = mid + 1
    else:
        return -1
print(binary_search(L,n))
