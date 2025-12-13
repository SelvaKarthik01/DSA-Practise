"""
Docstring for Arrays.Reverse Pairs

Count the Number of Reverse Pairs
i < j and a[i] > 2 * L[j]
[40,25,19,12,9,6,2] -> Output = 15

Another Apporach is take a element and go thorugh all elements and right and increase the Count 
TC -> O(n^2) keeping i as constant checking other elements that are greater than 2 * a[i]
SC -> O(1)

Time Complexity : O(logn) for recursion till we reach the end * O(n) for every element in the array + O(n) for the Extra Checking if we had
                  Total -> (O(n)+O(n))*O(logn) -> O(2nlogn) ->O(nlogn)
Space Complexity : O(n) for Temp space in Merge Sort

"""

def Merge(L,low,mid,high):
    i = low
    j = mid+1
    temp = []
    count = 0 
    for i in range(low,mid+1):
        while(j <= high and L[i] > 2*L[j]):
            j += 1
        count += (j -(mid+1))
    i = low 
    j = mid + 1
    while(i<=mid and j <= high):
        if L[i] <= L[j]:
            temp.append(L[i])
            i += 1
        elif L[i] > L[j]:
            temp.append(L[j])
            j += 1
    while(i<=mid):
        temp.append(L[i])
        i += 1
    while(j<=high):
        temp.append(L[j])
        j += 1
    L[low:high+1]=temp[:]
    return count
            
def Merge_Sort(L,low,high):
    count = 0 
    if low >= high:
        return count
    mid = (low + high)//2
    count += Merge_Sort(L,low,mid)
    count += Merge_Sort(L,mid+1,high)
    count += Merge(L,low,mid,high)
    return count

L = eval(input("Enter the List : "))

print(Merge_Sort(L,0,len(L)-1))
print(L)