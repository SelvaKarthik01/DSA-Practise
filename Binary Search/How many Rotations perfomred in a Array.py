# To Find out the Number of rotations performed in the array 
# For Ex : [15,18,2,3,6,12] Ans = 2 basically find the index of Pivot element 

def pivot(L):
    start = 0 
    end = len(L) -1 
    while(start < end):
        mid = start + (end - start)//2
        if L[mid] > L[end]:
            start = mid + 1
        else:
            end = mid 
    return start
L = eval(input("Enter the List : "))
print(pivot(L))