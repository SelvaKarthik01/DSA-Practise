"""
Docstring for Sorting Algorithms.Selection Sort

1) From the Array select or find the smallest element 
2) Replace the smallest with index i and increase i 
3) do it until we reach the last element 

Time Complexity : O(n^2)
Best Case: O(n^2)
Worst Case: O(n^2)
Space Complexity : O(1)
"""

L = eval(input("Enter the List : "))
for i in range(len(L)-1):
    smallest = i
    for j in range(i+1,len(L)):
        if L[j] < L[smallest]:
            smallest = j  # Selecting the Smallest Element from the Sub Array 
    L[i],L[smallest]=L[smallest],L[i] # Replacing it with the ith Index 
print((L))
        