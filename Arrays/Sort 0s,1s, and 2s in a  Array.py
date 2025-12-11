"""
Docstring for Arrays.Sorts 0s,1s, and 2s in a  Array

One Approach is used to Sort the array and hence this is done 
TC -> O(nlogn)
SC -> O(1)

Another Approach is to count the no. of zeros ones and two and then based on count fill the array 
TC -> O(n)-> For finding the count + O(n) ->. for filling the array -> O(2n)
SC -> O(n)


DUTCH NATIONAL FLAG ALGORITHM:

0     low-1 low    mid-1 mid      high high+1   n-1
|          ||          | |            ||         |
0000000....01111111....1[unsorted part]2....222222


Time Comeplxity -> O(n) -> Dutch National Flag Algorithm
Space Complexity -> O(1) -> Just Three Pointers here 

"""

L = eval(input("Enter the List : "))
low = mid = 0 
high = len(L)-1
while(mid <= high):
    if L[mid] == 0:
        L[low],L[mid]=L[mid],L[low]
        low += 1
    elif L[mid] == 2:
        L[high],L[mid]=L[mid],L[high]
        high -= 1
        continue
    mid+=1
print(L)

