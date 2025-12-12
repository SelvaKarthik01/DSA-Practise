"""
Docstring for Arrays.Majority Element II greater than N by 3

Now for Majority Element II Greater than N/3 times there is should be minimum of atleast 2 ans in the array 
Lets say we have 8 elements 8/3 = 2 so the coubtn should be strictly > 2that is min there can 3 
3 + 3 + 3= 9 != 8 so max only two elements can be present 


Another Approach is we know two elements will be there so go through the array and find the elemenst which is greater than N/3 and store 
TC -> O(n^2) -> consider a elements and find its count 
SC -> O(1)

Now count could be done with the help of the hashmap 
TC -> O(n)
SC -> O(n) -> at max all elements are saved with their count 

So the Optimal one would be the same as Moore's Voting Algorithm very simialr this time for two elements 

Time Complexity : O(n) for cancecllation counting part + O(n) for checking if its correct 
                  Total -> O(2n) -> O(n) 
Space Complexity : O(1)
"""

L = eval(input("Enter the List : "))  
count1 = 0 
count2 = 0 
el1=float("-inf")
el2 = float("-inf")
for i in range(len(L)):   # This is Moore's Voting Algorithm Simluated for 2 numbers as max there can be two numbers
    if count1 == 0 and L[i] != el2:
        el1 = L[i]
        count1 += 1
    elif count2 == 0 and L[i] != el1:
        el2 = L[i]
        count2 += 1
    elif L[i] == el1:
        count1 += 1
    elif L[i] == el2:
        count2 ++ 1
    else:
        count1-= 1
        count2 -= 1
        
# The Next Step is the checking part
count1 = 0 
count2 = 0
for i in range(len(L)):
    if L[i] == el1:
        count1 += 1
    elif L[i] == el2:
        count2 += 1
if len(L)//3 < count1:
    print(el1)
if len(L)//3 < count2 :
    print(el2)

        
