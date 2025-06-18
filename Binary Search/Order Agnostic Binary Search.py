# To Find the Binary search without given details of whether the given array is sorted in ascending or descending 
L = eval(input("Enter the List : "))
target = int(input("Enter the target Element to be searched : "))
if L[0] < L[-1]:
    key = "A"
else:
    key = "D"
def binary_search(L,n,key):
    start = 0
    end = len(L)-1
    while(start <= end):
        mid = start +(end-start)//2
        if L[mid] == n :
            return mid
        if L[mid] > target :
            if key == "A":
                end = mid - 1
            elif key == "D":
                start = mid + 1
        if L[mid] < target:
            if key == "A":
                start = mid + 1
            else:
                end = mid - 1
    else:
        return -1
print(binary_search(L,target,key))