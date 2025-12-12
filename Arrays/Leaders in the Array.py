"""
Docstring for Arrays.Leaders in the Array

Another Approach is to use take every element assume its leaders and check to its right and use a flg variable is true or not 
TC -> O(n^2) -> for every element towards the right 
SC -> O(1)

Leaders in an array are those that whose elements in the right are smaller
[10,22,12,3,0,6]
Leaders -> [22,12,6]

Time Complexity : O(n) -> Iterating from teh last till the first 
Space Compleixty : O(1) -> Auxiliary Space for storing the leaders O(n)

"""

L = eval(input("Enter the List : "))
leaders = [L[-1]]
for i in range(len(L)-2,-1,-1):
    if L[i] > leaders[-1]:
        leaders.append(L[i])

print(leaders)
    
