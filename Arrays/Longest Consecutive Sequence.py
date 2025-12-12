"""
Docstring for Arrays.Longest Consecutive Sequence

[102,4,100,1,101,3,2,1,1]
Longest Sequence is 1,2,3,4, -> 4 


Another Apporach is t0 take every element and check i+1 is present or not and increase the count and check which as the highest count
TC -> O(n^2) each element we checking the whole array 
SC-> O(1)

Another approach is using three variables last_smallest, i and count  and sorting the array 
[1,100,1,1,101,,4,3,102,103,2] -> [1,1,2,3,4,100,101,102,103]
We have three conditions here 
   if L[i] != last_smallest and L[i]-1 != last_smallest :
        It means new consequence si formed so we set count = 0 and last_smallest = L[i]
   if L[i] == last_smallest:
        i += 1 because repeation of teh bsame elemnt could be possible [1,1,1,1,2,3,3,3]
   if L[i] -1 == last_smallest:
        count += 1
        last_smallest = L[i]
    max_count = max(count,max_count)
    
TC -> O(nlogn)-> for sorting + O(n) -> for linear traversal -> O(nlogn)
SC -> O(1) -> just three varibles 

The Hack is to find the either the starting point or the ending poitn of the sequence thast why we use a hashmap
Time Complexity: O(n) -> for storing it in set + O(n) for finding every starting point + O(n) till we find the end point 
                      Total -> O(3n) -> O(n)
Space Complexity : O(n) -> for the hashmap 

"""
L = eval(input("Enter the List : "))
count = 0 
s = set(L)
# The key is to find the starting point 
max_count = 0
for i in s:
    if i-1 not in s: # This i is going to be our starting point [The opposite finding the end poitn is also possible]
        count = 1
        while(True):
            if i+1 in s: # Till we reach the end point 
                count += 1
                i += 1
            else:
                break 
    max_count = max(count,max_count)
print(max_count)
            