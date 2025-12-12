"""
Docstring for Arrays.Next Permutation in an Array

Another Approach is to recrusively find all the permutation of the number after sorting and storing it in sroted roder and then
a linear search to find the gievn array and get the next element which woudl be the next permuation

TC -> N! x N -> for finding all the permutation 
      N -> for linear search 
      O(N! x N + N) -> O(n!)
SC -> O(N) -> to store the sorted permuatations 

Algorithm: 

1) Find the longest Prefix that is possible by going from back and check the dip if L[i] < L[i+1]
2) Once we find the first dip or the breaking point now from the last till the breaking point find the first element 
greater than the breaking_point element (from last coz everything will be in sorted prder from last finding the first element greater 
would be the least min max value)
3) Now swap both the indexes
4) Now we need to reverse the Element from breaking_point + 1 till the in ascending order 
5) Now if there is no dip or breaking point only possible when it is last permutation then just reverse the List and return 

Time Complexity : O(n) -> for finding the breaking point 
                  O(n) -> for finding the min max value greater than breaking point 
                  O(n) -> for reversing the array from the breaking point 
                  Total -> O(3n)  -> O(n)
Space Complexity : O(1) not extra variables

"""


L = eval(input("Enter the List : "))
breaking_point = -1
for i in range(len(L)-2,-1,-1):
    if L[i] < L[i+1]:
        breaking_point = i
        break 

if breaking_point == -1:
    L.reverse()
    print(L)
else:
    for i in range(len(L)-1,breaking_point,-1):
        if L[i] > L[breaking_point]:
            max_val = i
            break
    L[breaking_point],L[max_val] = L[max_val],L[breaking_point]
    L[breaking_point+1:]=reversed(L[breaking_point+1:])
    print(L)
        