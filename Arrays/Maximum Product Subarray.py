"""
Docstring for Arrays.Maximum Product Subarray

Another Approach is to generate all the subarrays and multipliy the products and check if its max
TC-> O(n^2)
SC -> O(1)

Another Appraoch a Simulation of Kadanes Algorithm which is not intuitive
Same and Time and Space and Complexity as we this Algorithm 

Time Complexity : O(n)
Space Complexity : O(1)

"""
L = eval(input("Enter the List : "))
maxi = float("-inf")
prefix = 1 
suffix = 1 
for i in range(len(L)):
    if prefix == 0:
        prefix = 1
    elif suffix == 0:
        suffix = 1
    prefix *= L[i]
    suffix *= L[(len(L)-1)-i]
    maxi= max(maxi,max(prefix,suffix))
print(maxi)