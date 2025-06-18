L = eval(input("Enter the List : "))
target = int(input("Enter the target : "))

def find_pivot(L):
    start = 0
    end = len(L) - 1
    while start < end:
        mid = (start + end) // 2
        if L[mid] > L[end]:  
            start = mid + 1
        else:  
            end = mid
    return start  

def binary_search(L, target, start, end):
    while start <= end:
        mid = (start + end) // 2
        if L[mid] == target:
            return mid
        elif L[mid] < target:
            start = mid + 1
        else:
            end = mid - 1
    return -1

# Edge case for 1 or 2 elements
if True:
    pivot = find_pivot(L)
    print("Pivot found at index:", pivot)

    # Search left side
    if L[pivot] <= target <= L[-1]:
        print(binary_search(L, target, pivot, len(L) - 1))
    else:
        print(binary_search(L, target, 0, pivot - 1))