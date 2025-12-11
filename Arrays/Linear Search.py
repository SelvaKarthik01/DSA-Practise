"""
Docstring for Arrays.Linear Search

Recursive Linear Search Solution

def recurisive_linear_search(L,i,target):
    if L[i] ==len(L):
        return False
    if L[i] == target:
        return True 
    return recursive_linear_search(L,i+1,target)

Time Comeplexity : O(n)
Space Complexity : O(1)

"""

L= eval(input("Enter the Number : "))
target = int(input("Enter the target Element : "))
for i in range(len(L)):
    if L[i] == target:
        print(i)
        break 
else:   
    print(-1)