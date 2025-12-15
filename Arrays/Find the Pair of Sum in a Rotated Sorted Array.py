"""
Docstring for Arrays.Find the Pair of Sum in a Rotated Sorted Array
"""
def Binary_Search(L):
    ans =float("inf")
    index = -1
    low = 0 
    high = len(L)-1
    while(low <= high):
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
    return index 
L = eval(input("Enter the List : "))
lowest = Binary_Search(L)
print(lowest)
    
target = int(input("Enter the Target : "))
if L[lowest] + L[len(L)-1] >= target:
    n = 0
else:
     n = (len(L)-1)-(lowest-1)
highest = len(L)-1
while(lowest<=highest):
    if L[lowest] + L[highest-n] == target:
        print("True")
        break 
    elif L[lowest] + L[highest-n] > target:
        highest -= 1
    else:
        lowest += 1
else:
    print(False)