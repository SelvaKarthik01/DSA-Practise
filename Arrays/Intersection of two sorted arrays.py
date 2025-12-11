"""
Docstring for Arrays.Intersection of two sorted arrays

Another Approach is to use a visited array in one of the arrays and check if we have check it or not until the first array reaches the end 
TC -> O(n)
SC -> O(n) for the visited array set 


Time Complexity : O(n)
Space Complexity : O(1) -> Auxiliary Space O(n) for storing the ans array 

"""

L1 = eval(input("Enter the List 1 : "))
L2 = eval(input("Enter the List 2 : "))
i = 0 
j = 0
ans = [] 
while(i < len(L1) and j < len(L2)):
    if L1[i] != L2[j] and L1[i] < L2[j]:
        i += 1
    elif L1[i] != L2[j] and L2[j] < L1[i]:
        j += 1
    if L1[i] == L2[j]:
        ans.append(L1[i])
        i +=1 
        j+= 1 
print(ans)