"""
Docstring for Binary Search.First and Last Occurences of the Array

[2,4,6,8,8,8,11,13] -> 3 First Occurence and 5 is the Last Occurence 

Another Apporach is Linea rSearch form start tillwe reach the target and from end we reach the the Target 
TC ->  O(n)
SC -> O(1)


Lower Bound : Smallest element >= target 
Upper Bound : Smallest Element > target

Using Just Binary Search without Lower and Upper Bound kinda thingy 

class Solution(object):
    def searchRange(self, L, target):
        def Binary_Search_last(L,target):
            ans = -1 
            low = 0 
            high = len(L)-1
            while(low <= high):
                mid = low + (high-low)//2
                if L[mid] == target:
                    ans = mid 
                    low = mid + 1
                elif L[mid] > target:
                    high = mid -1
                else:
                    low = mid + 1
            return ans 
        def Binary_Search_first(L,target):
            ans = -1 
            low = 0 
            high = len(L)-1
            while(low <= high):
                mid = low + (high-low)//2
                if L[mid] == target:
                    ans = mid 
                    high = mid - 1
                elif L[mid] < target:
                    low = mid + 1
                else:
                    high = mid -1

            return ans 
        first = Binary_Search_first(L,target)
        last = Binary_Search_last(L,target)
        return [first,last]


Time Complexity : O(logn)
Space Complexity : O(1)

"""
def Lower_Bound(L,target):
    low = 0
    high = len(L)-1
    ans = len(L)
    while(low <= high):
        mid = low + (high-low)//2
        if L[mid] >= target:
            ans = mid 
            high = mid - 1
        else:
            low = mid + 1
    return ans 
def Upper_Bound(L,target):
    low = 0
    high = len(L)-1
    ans = len(L)
    while(low <= high):
        mid = low + (high-low)//2
        if L[mid] > target:
            ans = mid 
            high = mid - 1
        else:
            low = mid + 1
    return ans
L = eval(input("Enter the List : "))
target = int(input("Enter the Element : "))
first = Lower_Bound(L,target)
if L[first] != target and first== len(L):
    print(-1,-1)
else:
    print(first,Upper_Bound(L,target)-1)