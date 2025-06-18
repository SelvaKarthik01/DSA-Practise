# To Find the Peak Element in a Bitonic Array 

def binary_search(L):
    start = 0 
    end = len(L)-1
    while(start < end):
        mid = start + (end -start)//2
        if L[mid] > L[mid + 1]:
            #decs part of array
            end = mid
        else:
            start = mid + 1
    return start
L = eval(input("Enter the List : "))
print(binary_search(L))