"""
Docstring for Arrays.Merge Two Sorted Arrays with Constant Space

Normal Merging of Arrays as we do in Merge Sort 
TC -> O(n+m)
SC -> O(n+m)

Another Approach is by push all high elements into one array and lower elements into another 
[1,3,5,7] [2,4,6,8]
We start from highest of arr1 and lowest and arr 2 and swap until we find a element arr1 which is smaller than the arr2
[1,3,4,2] [7,5,6,8] again sorting this and combing we have done the problem

class Solution(object):
    def merge(self, nums1, m, nums2, n):
        i = m-1 
        j = 0
        while(i >= 0 and j < n):
            if nums1[i] > nums2[j]:
                nums1[i],nums2[j] = nums2[j],nums1[i]
            i-= 1
            j += 1
        nums1[:m]=sorted(nums1[:m])
        nums2.sort()
        for i in range(len(nums2)):
            nums1[m+i]=nums2[i]

TC -> O(n) + O(nlogn) + O(nlogn)
     Total -> O(n) + O(2nlogn) -> O(nlogn)
SC -> O(1) -=-> Just Auxiliary Space of two given Sorted Arrays 



This method is what is used in Shell Sort also called as thew Gap method we reduce the gap and swap elements for each Iterations

Time Complexity : O(logn) for gap as it is divding by 2 for each iteration * O(n) for iteration 
                  Total -> O(nlogn)
Space Complexity : O(1)

"""
import math 

L1 = eval(input("Enter the First List : "))
L2 = eval(input("Enter the Second List : "))
gap = math.ceil((len(L1)+len(L2))/2)

def swapNumber(L1,L2,ind1,ind2):
    if L1[ind1] > L2[ind2]:
        L1[ind1],L2[ind2]=L2[ind2],L1[ind1]
    
while(True):
    left = 0 
    right = left + gap 
    while(right < (len(L1)+len(L2))):
        if (right < len(L1)):      # When Both Left and Right are present in L1
            swapNumber(L1,L1,left,right)
        elif (left >= len(L1)):     # When Both Left and Right are present in L2
            swapNumber(L2,L2,left-len(L1),right-len(L1))
        else:                       # When Left is in L1 and right is in L2
            swapNumber(L1,L2,left,right-len(L1))
        left += 1
        right += 1
    if gap == 1:
        break 
    gap = math.ceil(gap/2)
print(L1)
print(L2)
    
                
                
        
    
    

            
        
    