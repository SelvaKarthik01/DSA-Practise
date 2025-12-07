"""
Docstring for Recursions.Permutation kth Sequence

60. Permutation Sequence
Hard
Topics
premium lock icon
Companies
The set [1, 2, 3, ..., n] contains a total of n! unique permutations.

By listing and labeling all of the permutations in order, we get the following sequence for n = 3:

"123"
"132"
"213"
"231"
"312"
"321"
Given n and k, return the kth permutation sequence.

Example 1:

Input: n = 3, k = 3
Output: "213"
Example 2:

Input: n = 4, k = 9
Output: "2314"
Example 3:

Input: n = 3, k = 1
Output: "123"
 

Constraints:

1 <= n <= 9
1 <= k <= n!
"""


n = int(input("Enter the Number : "))

k = int(input("Enter the Value of K : "))

L = [i for i in range(1,n+1)]

def factorial(n):
    if n == 0:
        return 1 
    return n * factorial(n-1)

def recursion(n,L,k,ans):
    if n==0:
        return 
    num_comb = factorial(n-1)
    first_num_index = k // num_comb
    ans.append(L[first_num_index])
    L.remove(L[first_num_index])
    k = k % num_comb
    recursion(n-1,L,k,ans)
ans = []
recursion(n,L,k-1,ans)
print(ans)
        
