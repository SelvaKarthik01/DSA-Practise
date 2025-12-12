"""
Docstring for Arrays.Move all zeros to the end of Array

Another approach is to store all the non zero numbers in a set or array and then set all other elements in as zero 

Collecting all non-zeros -> O(n)
Setting into non-zeros into the front -> O(n)
Remaining all as zeros -> O(n)
Total -> O(3n) -> O(n)

SC -> O(n) -> For Storing the elements in the array 

Time Complexity : O(n) -> Just running tbhrough the end of loop once 
Space Complexity : O(1) -> No extra space just two pointer variables 

"""
L = eval(input("Enter the List : "))
left = 0 
right = len(L)-1
while(left < len(L) and right >= 0 and left < right):
    if L[left] == 1:
        left += 1
    elif L[right] == 0:
        right -= 1 
    else:
        L[left],L[right]=L[right],L[left]
        left += 1
        right -= 1  
print(L) 