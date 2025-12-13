"""
Docstring for Arrays.Merge Overlapping Sub Intervals

Another Apporach is to sort the Array and check if the start interval and less than the previous end interval if yes put into it 
increasing the end interval of the pointer 
Now if the start is greater a new interval is formed so move the pointer to the and do the same
TC- -> O(nlogn) for sorting + O(n^2) for keeping pointer as constant and then checking all intervals that overlap 
    -> Total -> O(nlogn) + O(n^2) -> O(n^2)
SC -> O(n) for saving all the intervals 

Time Complexity : O(nlogn) for sorting + O(n) for traversing and updating the intervals
                  Total -> O(nlogn) + O(n) -> O(nlogn) 
Space Complexity : O(n) for saving all the unique intervals
 
"""
L = eval(input("Enter the Intervals : "))
L.sort()
ans = []
pointer = L[0]
for i in range(1,len(L)):
    if L[i][0] <= pointer[1]:
        start_interval = min(L[i][0],pointer[0])
        end_interval = max(L[i][1],pointer[1])
        pointer = (start_interval,end_interval)
    elif L[i][0] > pointer[1]:
        ans.append(pointer)
        pointer = L[i]
ans.append(pointer)
print(ans)
        