"""
Docstring for Recursions.All Possible Permutations

Example 1:

Input: nums = [1,2,3]
Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
Example 2:

Input: nums = [0,1]
Output: [[0,1],[1,0]]
Example 3:

Input: nums = [1]
Output: [[1]]

"""

L = eval(input("Enter the List : "))

ans = []
def recursion(L,i,ans):
    if i == len(L):
        ans.append(list(L))
        return 
    for k in range(i,len(L)):
        L[i],L[k]=L[k],L[i]
        recursion(L,i+1,ans)
        L[k],L[i]=L[i],L[k]
recursion(L,0,ans)
print(ans)
        