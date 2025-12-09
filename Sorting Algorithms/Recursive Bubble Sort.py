L = eval(input("Enter the List : "))

def HelperBubbleSort(L,j,n):
    if j == n:
        return 
    if L[j] > L[j+1]:
        L[j],L[j+1]=L[j+1],L[j]
    HelperBubbleSort(L,j+1,n)
    

def recursiveBubbleSort(L,n):
    if n ==0:
        return 
    HelperBubbleSort(L,0,n-1)
    recursiveBubbleSort(L,n-1)
recursiveBubbleSort(L,len(L))
print(L)
    
