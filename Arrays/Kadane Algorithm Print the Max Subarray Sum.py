"""
Docstring for Arrays.Kadane Algorithm Print the Max Subarray Sum

Time Complexity : O(n)
Space Complexity : O(1)
"""

L = eval(input("Enter the List : "))
anss = 0 
anse = len(L)-1
sum = float("-inf")
max_sum = float("-inf")
for i in range(len(L)):
    if L[i] > sum+L[i]:
        sum = L[i]
        anss = i
    else:
        sum += L[i]
    if sum > max_sum:
        max_sum= sum 
        anse = i 
print(max_sum)
print(L[anss:anse+1])