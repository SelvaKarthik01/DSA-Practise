"""
Docstring for Sorting Algorithms.Bubble Sort

Key is on every iteration the max eleement is added to the Last 

1) Compare the Adjacent element is L[j] > L[j+1] Swap and move j 
2) now the last max eleent is added at last now loop till n-1, n-2, n-1-i times ....
3) We can optimise this when no swaps have been found we can include a didswap flag variables and stop furthur iterations

Time Complexity: O(n^2)
Space Complexity : O(1) 
"""

L = eval(input("Enter the List : "))
for i in range(len(L)):
    didswap = 0
    for j in range(len(L)-1-i):
        if L[j] > L[j+1]:
            L[j],L[j+1]=L[j+1],L[j]
            didswap = 1
    if didswap == 0:
        break
        
print(L)