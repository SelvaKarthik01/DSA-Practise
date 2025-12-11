"""
Docstring for Arrays.Check if an Array is sorted or not

Time Complexity : O(n) -> Only once iterating the array till the end
Space Complexity : O(1) -> no Extra variables 
"""
L = eval(input("Enter the List : "))
for i in range(len(L)-1):
    if L[i] > L[i+1]:
        print("False") 
        break
else:
    print("True")