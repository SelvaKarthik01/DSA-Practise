"""
Docstring for Arrays.Count Inversions

Count Inversions 
i < j and a[i] > a[j]
[5,3,2,4,1] -> [5,1],[5,3],[5,2].....[4,2] not possible as i > j

One Approach is to go through all the elements and in the array and check if lesser 
TC -> O(n^2) keeping i as constant we are checking the whole arrya for elements lesser 
SC -> O(1)

Now the key is take every element and check the next element and so on 
Why can't we divide the array into two and do the same as seen in Merge Sort 
[5] [3] we have the count as we move up the recursion tree [3,5] [2] so automatically we are counting it while we are merging 

Time Complexity : O(nlogn)
Space Complexity : O(n)

"""

def Merge(L,low,mid,high):
    i = low 
    j = mid+1
    ans = []
    count = 0
    while(i <= mid and j <= high):
        if L[i] <= L[j]:
            ans.append(L[i])
            i += 1
        elif L[j] < L[i]:
            ans.append(L[j])
            count += mid-i+1
            j += 1
    while(i <= mid):
        ans.append(L[i])
        i += 1 
    while(j <= high):
        ans.append(L[j])
        j += 1
    L[low:high+1]=ans[:]
    return count
            

def Merge_Sort(L,low,high):
    count = 0
    if low >= high:
        return count 
    mid = (low+high)//2
    count += Merge_Sort(L,low,mid)
    count += Merge_Sort(L,mid+1,high)
    count += Merge(L,low,mid,high)
    return count
    

L = eval(input("Enter the List : "))
print(Merge_Sort(L,0,len(L)-1))



