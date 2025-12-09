L=eval(input("Enter the List : "))

def HelperInsertionSort(L,j):
    if j <=1:
        return 
    if L[j] < L[j-1]:
        L[j],L[j-1]=L[j-1],L[j]
    HelperInsertionSort(L,j-1)
def recursiveInsertionSort(L,i,n):
    if i == n:
        return 
    HelperInsertionSort(L,i) 
    recursiveInsertionSort(L,i+1,n)
    
    
recursiveInsertionSort(L,0,len(L))
print(L)