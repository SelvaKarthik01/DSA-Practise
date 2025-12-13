"""
Docstring for Arrays.Count No. of Subarrays with XOR as k

Another Approach is to find the find all the subarrays and xor the operations and find if its = k or not
TC -> O(n^2) keeping i as constant we are looping from i+1 till len(L)-1 and keeping xor = i ^ j 
SC -> O(1)

Time Complexity : O(n)
Space Complexity : O(1)
""" 
L = eval(input("Enter the List : "))
k = int(input("Enter the Target XOR : "))
xor = 0 
d = {0:1} # To make sure if it xor is zero then also it should be considered
count = 0
for i in range(len(L)):
    xor ^= L[i]
    if xor^k in d:
        count += d[xor^k]
    d[xor] = d.get(xor,0)+1
print(count)