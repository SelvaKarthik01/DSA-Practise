"""
Docstring for Sorting Algorithms.Insertion Sort

Pick a element in the ith window box and put the element in the correct possition from swapping from last after including that element in the window

1) Consider the window from 0 to i
2) Consider the j element from last to 1 (exlcuding 0)
3) Compare the elements to the right 
4) If smaller that is L[j] < L[j-1] --> Swap 
5) Now do the swapping till we reach j == 0 
6) Do the Same rprocess for i times 

Time Complexity : O(n^2)
Best Case : O(n)
Worst Case : O(n)
Space Complexity : O(1)

"""

L = eval(input("Enter the List : "))
for i in range(len(L)):
    j = i 
    while(j > 0 and L[j-1] > L[j]):
        L[j-1],L[j] = L[j],L[j-1]
        j -= 1
print(L)
    