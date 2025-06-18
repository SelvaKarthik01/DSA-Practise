# TO Find the First and Last Position fo a traget element in a  Array 
# For Example L = [5,7,7,7,7,8,8,10]
# Target First Position = 1
# Target last position = 4
L = eval(input("Enter the List : "))
target = int(input("Enter the Target element"))
def binary_search_ceil(L,target):
    start = 0 
    end = len(L) -1
    while(start <= end):
        mid = start + (end - start)//2
        if (L[mid] > target):
            end = mid - 1
        else:
            start = mid + 1
    return start
def binary_search_floor(L,target):
    start = 0 
    end = len(L) -1
    while(start <= end):
        mid = start + (end - start)//2
        if (L[mid] < target):
            start = mid + 1
        else:
            end = mid - 1
    return end

def binary_search(L,target):
    start = 0 
    end = len(L) -1
    while(start <= end):
        mid = start + (end - start)//2
        if (L[mid] < target):
            start = mid + 1
        if L[mid] > target:
            end = mid - 1
        if L[mid] == target:
            return mid
    return -1
if binary_search(L,target) == -1 :
    ans = [-1,-1]
else:
    ans = [binary_search_floor(L,target)+1,binary_search_ceil(L,target)-1]
print(ans)
    


    


