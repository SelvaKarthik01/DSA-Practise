# To Perfomr Binary serach in a Rortated sorted Array using Recursion 

def binary_search(L,target,start,end):
    if start > end:
        return -1
    mid = start + (end - start)//2
    if L[mid] == target:
        return mid
    if L[mid] > L[start]:
        if L[start] <= target <= L[mid]:
            return binary_search(L,target,start,mid-1)
        else:
            return binary_search(L,target,mid+1,end)
    if (target >= L[mid] and target <= L[end]) :
        return binary_search(L,target,mid +1,end)
    else:
        return binary_search(L,target,start,mid-1)
        

L = eval(input("Enter the List : "))
target = int(input("Enter the target Element : "))
print(binary_search(L,target,0,len(L)-1))