"""
Docstring for Arrays.Find the number which appears once

Most widely used  solution would be using Single Number I that is Xor operations and returning
TC -> O(n)
SC -> O(1)

Time Complexity: O(n) -> For finding the actual sum of the given array 
Space Complexity: O(1)

"""

L = eval(input("Enter the List : "))
n = (len(L)+1)//2
expected_sum = 2*((n*(n+1))//2)
actual_sum = sum(L)
missing_num = expected_sum - actual_sum 
print(missing_num)