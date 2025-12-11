"""
Docstring for Arrays.Remove duplicate elements in-place from the array

Another approach is to put all element into a set -> O(logn)
and then convert the set into a List and return (Not in-place)
TC-> O(logn)+O(n) -> O(n)
Space Complexity ->O(n)

Time Complexity : O(n) -> Running till the end
Space Complexity : O(1) -> No extra spaces used in-place 

"""
L = eval(input("Enter the List : "))
i = 0 
j = i + 1
while(j < len(L)):
    if L[i] != L[j]:
        L[i+1]=L[j]
        i += 1
    j += 1
for j in range(i+1,len(L)):
    L[j]="_"
print(L)
print("No of Unique elements: ",i+1)
