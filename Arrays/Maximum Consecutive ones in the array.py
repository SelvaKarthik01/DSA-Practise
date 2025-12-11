"""
Docstring for Arrays.Maximum Consecutive ones in the array

Time Complexity : O(n) -> Just iterating till the end with one for loop 
Space Complexity : O(1)

"""

L = eval(input("Enter the List : "))
max_cons = 0 
cons = 0
for i in range(len(L)):
    if L[i] == 1:
        cons += 1
    elif L[i] != 1:
        max_cons = max(cons,max_cons)
        cons = 0 
max_cons = max(cons,max_cons)
print(max_cons)
    