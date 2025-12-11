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
L = eval(input("Enter the Array : "))
non_zero=0
zero = 0 
while(non_zero != len(L)):
    while(zero < len(L) and L[zero]!=0):
        zero += 1
    non_zero = zero + 1
    while(non_zero < len(L) and L[non_zero]==0):
        non_zero += 1
    if non_zero < len(L) and zero <len(L):
        L[zero],L[non_zero]=L[non_zero],L[zero]
print(L)
    