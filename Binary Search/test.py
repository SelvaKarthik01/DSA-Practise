L = eval(input("Enter the List : "))
target = int(input("Enter the Target Element : "))
def binary_search(L,target):
    start = 0 
    end = len(L)-1
    while (start <= end):
        mid =start + (end-start)//2
        if L[mid] > target:
            end = mid -1
        else:
            start = mid + 1
    return start,end 
start,end = binary_search(L,target)
ans = [L[end],L[start]]
print(ans)        