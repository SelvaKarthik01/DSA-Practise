"""
Docstring for Arrays.Left rotate the array by one place

[1,2,3,4,5] -> [2,3,4,5,1]

Time Complexity: O(n)
Space Complexity: O(1) (in-place)

"""
L = eval(input("Enter the List : "))
temp = L[0]
for i in range(1,len(L)):
    L[i-1] = L[i]
L[-1] = temp 
print(L)