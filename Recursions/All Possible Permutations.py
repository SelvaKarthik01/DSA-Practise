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
marker = [0]*(len(L))
def recursion(L,i,marker,ds,ans):
    if i == len(L):
        ans.append(list(ds))
        return 
    for k in range(len(L)):
        if marker[k] != 1:
            ds.append(L[k])
            marker[k]=1
            recursion(L,i+1,marker,ds,ans)
            ds.pop()
            marker[k]=0
recursion(L,0,marker,[],ans)
print(ans)