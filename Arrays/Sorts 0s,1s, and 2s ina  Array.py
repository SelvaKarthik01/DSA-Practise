L = eval(input("Enter the List "))
low = 0
mid = 0
high = len(L)-1 
while(mid <=high):
    if L[mid] == 0:
        L[low],L[mid] = L[mid],L[low]
        low += 1
        mid += 1
    elif L[mid] == 1:
        mid += 1
    elif L[mid] == 2:
        L[mid],L[high] = L[high],L[mid]
        high -= 1
print(L)
        