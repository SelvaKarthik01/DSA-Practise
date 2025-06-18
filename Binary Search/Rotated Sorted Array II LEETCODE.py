L = eval(input("Enter the Number : "))
target = int(input("Enter the target Element : "))
def pivot(L):
    start = 0 
    end = len(L)-1
    while(start < end):
        mid = start + (end - start)//2
        if L[mid] > L[end]:
            start = mid + 1
        else :
            end = mid
    return start
def binary_search(L,target,start = 0 ,end = len(L)-1):
    while(start <= end):
        mid = start + (end - start)//2
        if L[mid] == target:
                return "true"
        if L[mid] > target:
            end = mid -1 
        if L[mid] < target:
            start = mid + 1
    return "false"

peak = pivot(L)
print(peak)
if L[0] <= target <= L[peak-1]:
    print("Left")
    print(binary_search(L,target,0,peak-1))
else:
    print("Right")
    print(binary_search(L,target,peak))
# [1,1,1,1,1,1,1,1,1,1,1,1,1,2,1,1,1,1,1]
    