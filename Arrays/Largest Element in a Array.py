"""
Docstring for Arrays.Largest Element in a Array

Another approach is to sort the array and use the L[-1] -> O(nlogn) for sorting 

Time Complexity: O(n) -> Traversing through all the elements 
Space Complexity: O(1) -> No extra use of arrays just one variable

"""
L = eval(input("Enter the List : "))
largest = float("-inf")
for i in range(len(L)):
    if L[i] > largest:
        largest = L[i]
print(largest)
