# Quick Sort Notes 
"""
Docstring for Sorting Algorithms.Quick Sort

1) Pick a Pivot Element and place it in its Correct Position 

-> First Element
-> Last Element 
-> Middle Element 
-> Random Elemetn from the Array 

Any Element from this can be Taken as a Pivot Element 


2) Smaller elements of the Pivot to the left adn Larger Element to the right and do the Divide conquer the same like Merge Sort 

Time Complexity : O(nlogn)
Space Complexity : O(1)
"""


def Partition(L,low,high):
    pivot = L[low]
    i= low
    j = high
    while(i < j):
        while(i <= high and L[i]<=pivot):
            i += 1
        while(j >= low and L[j]>pivot):
            j -= 1
        if (i < j):
            L[i],L[j] = L[j],L[i]
    L[j],L[low]=L[low],L[j] 
    return j
    
def Quick_Sort(L,low,high):
    if low >= high:
        return 
    partition = Partition(L,low,high)
    Quick_Sort(L,low,partition-1)
    Quick_Sort(L,partition+1,high)
    

L = eval(input("Enter the List : "))
Quick_Sort(L,0,len(L)-1)
print(L)