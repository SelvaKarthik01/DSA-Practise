"""
Docstring for Sorting Algorithms.Merge Sort

1) Take a Element and Divide it into two 

2) Apply the Same Megere sort Recursivly for left adn right array unitl we have only on element in the arry  (low >= high)

3) Once the Array is sorted we Merge them using Merge

-> Take a Temp array and two pointer for the both the left and Right array and place the smallest Element 
-> copy the Temp Array inot the Original Array for sorting


Time Complexity: O(nlogn)
Space Complexity: O(n)
"""


def Merge(L,low,mid,high):
    temp = []
    i = low
    j = mid + 1
    while(i <= mid and j <= high):
        if L[i] <= L[j]:
            temp.append(L[i])
            i += 1
        elif L[i] > L[j]:
            temp.append(L[j])
            j += 1
    while(i <= mid):
        temp.append(L[i])
        i += 1
    while(j<= high):
        temp.append(L[j])
        j += 1
    L[low:high+1]=temp
            
def Merge_sort(L,low,high):
    if low >= high:
        return 
    mid = (low + high)//2
    Merge_sort(L,low,mid)
    Merge_sort(L,mid+1,high)
    Merge(L,low,mid,high)
    
    
L = eval(input("Enter the List : "))     
Merge_sort(L,0,len(L)-1)
print(L)