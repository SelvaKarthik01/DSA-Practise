"""
Docstring for Arrays.Four Sum

Another Apporach that is Brute Force 
TC-> O(n^4)
SC->O(1)

Another Approach using Hashmap very similar to the three Sum and Prefix 
TC-> O(n^3)
SC->O(1)

Time Complexity : O(n^3) -> keeping i ans constant, keeping j as constant, and moving k and l as pointers  + O(nlogn) for sorting
Space Complexity : O(1) -> Auxiliary Space O(n) fro storing the quadruples
"""
L = eval(input("Enter the List : "))
target = int(input("Enter the Target : "))
L.sort()
i = 0 
ans = []
while(i < len(L)):
    j = i + 1
    while(j < len(L)):
        k = j + 1
        l = len(L)-1
        while(k < len(L) and l >= 0 and k < l):
            if L[i]+L[j]+L[k]+L[l] < target:
                k += 1
            elif L[i] + L[j] + L[k] + L[l] > target:
                l -= 1
            elif L[i]+L[j]+L[k]+L[l] == target:
                ans.append([L[i],L[j],L[k],L[l]])
                temp = L[k]
                while(k < l and L[k]==temp):
                    k +=1 
                temp = L[l]
                while(k < l and L[l]==temp):
                    l -= 1 
        temp = L[j]
        while(j < len(L) and L[j] == temp):
            j += 1
    temp = L[i]
    while(i < len(L) and L[i]==temp):
        i += 1
print(ans)
                