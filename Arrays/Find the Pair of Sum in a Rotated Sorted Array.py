"""
Docstring for Arrays.Find the Pair of Sum in a Rotated Sorted Array

Time Complexity : O(logn) for finding the min element in the rotated Sorted Array + O(n) for finding the Pair of Sum 
                  Total : O(logn) + O(n) -> O(n)
Space Complexity : O(1)

"""
def Binary_Search(L):
    ans = float("inf")
    index = -1
    low = 0 
    high = len(L)-1
    while(low <= high):
        mid = low + (high-low)//2
        if L[low] <= L[mid]:
            if L[low] < ans:
                ans = L[low]
                index = low 
            low = mid + 1 
        else:
            if L[mid] < ans:
                ans = L[mid]
                index = mid 
            high = mid -1 
    return index 
            
def Pair_of_sum(L,target,left,right):
    iterations = 0
    while(iterations != len(L)-1):
        if left == len(L):
            left = 0 
        if right == -1:
            right = len(L)-1
        if L[left] + L[right] == target:
            return True 
        elif L[left] + L[right]  > target:
            right -= 1
        elif L[left] + L[right] < target:
            left += 1
        iterations += 1
    return False 
               
L = eval(input("Enter the Element : "))
target = int(input("Enter the Target Sum : "))
left = Binary_Search(L)
right = left - 1
print(Pair_of_sum(L,target,left,right))

    