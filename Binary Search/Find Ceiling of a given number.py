# TO Find the Ceiling a given Traget Number ina  Array using Binary Search 

L = eval(input("Enter the List : "))
target = int(input("Enter the target element : "))
def binary_search(L,n):
    start = 0 
    end = len(L)-1
    while(start <= end):
        mid = start + (end-start)//2
        if L[mid] > target:
            end = mid - 1
        else :
            start = mid + 1
    return L[start]
print(binary_search(L,target))
            