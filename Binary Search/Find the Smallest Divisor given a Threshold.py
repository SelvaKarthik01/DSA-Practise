"""
Docstring for Binary Search.Find the Smallest Divisor given a Threshold

Time Complexity : O(nlogn)
Space Compleixty : O(1)
"""
import math
def Sum_Divisor(L,n):
    sum = 0 
    for i in range(len(L)):
        sum += math.ceil(L[i]/float(n))
    return sum 

def Binary_Search(L,threshold):
    low = 1 
    high = max(L)
    while(low <= high):
        mid = low + (high-low)//2
        if Sum_Divisor(L,mid) <= threshold:
            high = mid - 1
        else:
            low = mid + 1
    return low 

L = eval(input("Enter the List : "))
threshold = int(input("Enter the Threshold : "))
print(Binary_Search(L,threshold))