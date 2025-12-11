"""
Docstring for Arrays.Two Sum

Another Approach is to generate all the subarrays of two elements and find the those with sum = target 
TC-> O(n^2)
SC -> O(1)

Another apporach is very similar to prefix sum look at the target - curr and see if we have seen earlier if yes increase count 
TC -> O(n) 
SC -> O(n)

Time Complexity : O(nlogn) for sorting the array 
Space Compleixty : O(1) -> Just two pointer varaibles 

"""


L = eval(input("Enter the List : "))
target = int(input("Enter the Target Sum : "))
L.sort()  # Greedy Approach 
i = 0 
j = len(L)-1
sum = 0
while(i < j):
    sum = L[i]+ L[j]
    if sum > target:
        j -=1 
    elif sum < target :
        i += 1
    elif sum == target :
        print("True")
        break 
else:
    print("False")
