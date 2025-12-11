"""
Docstring for Arrays.Second Largest Element in a Array

Another approach is to sort and return L[-2] -> O(nlogn)
Another approach is first go thourgh the array find the Largest element O(n) and then find the second largest less than largest O(n)
--> O(2n)

Time Complexity : O(n) -> Iterating only one time till the end 
Space Complexity : O(1) -> just two variables
"""

L = eval(input("Enter the List : "))
largest = -1
second_largest = -1
for i in range(len(L)):
    if L[i] > largest:
        second_largest = largest
        largest = L[i]
    elif L[i] < largest and L[i] > second_largest:
        second_largest = L[i]
print(second_largest)
    
        