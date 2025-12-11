"""
Docstring for Arrays.Rearrange Positives and Negatives in a Array

One Approach is to iterate thourgh the array adn have extra ans array and for +ve number add at odd and vice versa

class Solution(object):
    def rearrangeArray(self, L):
        ans = [0]*len(L)
        pos = 0 
        neg = 1
        for i in range(len(L)):
            if L[i] > 0:
                ans[pos] = L[i]
                pos += 2
            else:
                ans[neg] = L[i]
                neg += 2

        return ans

TC-> O(n) -> Juts Iterating through the Loop 
SC -> O(n) -> For Storing the answer Array 

Time Complexity : O(n^2) -> Not Optimal but constant space
Space Complexity : O(1) -> in-place 
         
"""

L = eval(input("Enter the List : "))
i = 0
while(i < len(L)):
    if i & 1 == 0:
        if L[i] < 0:
            for j in range(i+1,len(L),2):
                if L[j] > 0:
                    L[i],L[j]=L[j],L[i] 
                    break
    else:
        if L[i] > 0:
            for j in range(i+1,len(L),2):
                if L[j] < 0:
                    L[i],L[j]=L[j],L[i]
                    break 
            
    i += 1
print(L)
        