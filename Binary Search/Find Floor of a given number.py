# TO Find  the Floor of then given number using Binary Search for the traget numebr which is very similar to the Ceil
L = eval(input("Enter the List : "))
n = int(input("Enter the target element : "))
def binary_search(L,target):
    start = 0
    end = len(L)-1
    while(start <= end):
        mid = start + (end -start)//2
            
        if L[mid] < target:
            start = mid + 1
        else:
            end = mid - 1
    return L[end]
print(binary_search(L,n))
        