"""
Docstring for Hashing.Counting Frequencies of an element in Array

Counting Frequencies of Array Elements


0

100
Easy

Given an array nums of size n which may contain duplicate elements.



Rreturn a list of pairs where each pair contains a unique element from the array and its frequency in the array.



You may return the result in any order, but each element must appear exactly once in the output.


Examples:
Input: nums = [1, 2, 2, 1, 3]

Output: [[1, 2], [2, 2], [3, 1]]

Explanation:

- 1 appears 2 times

- 2 appears 2 times

- 3 appears 1 time

Order of output can vary.
"""

L = eval(input("Enter the List : "))
hash = {}
for i in L:
    hash[i] = hash.get(i,0) + 1

ans = []
for i in hash:
    ans.append([i,hash[i]])
print(ans)