"""
Docstring for Arrays.Left Rotate a array d times

Use the same approach of how we left rotate by 1 time now this time d times keep j = i + d and do the same and save all L[:d] 
elements in a temp array 

def rotateArray(arr: list, k: int) -> list:
    temp = []
    k = k % len(arr)
    j = k
    for i in range(k):
        temp.append(arr[i])
    while(j < len(arr)):
        arr[j-k] = arr[j]
        j += 1
    for i in range(len(temp)):
        arr[len(arr)-k+i] = temp[i]
    return arr 

TC -> O(n-d) + O(d) + O(d)-> O(n)
SC -> O(d)

Time Complexity : O(d) + O(n-d) + O(n) -> O(2n) [Higher than the previous one]
Space Complexity : O(1)
"""

L = eval(input("Enter the List : "))
d = int(input("Enter the value for d : "))
d = d % len(L)
L[:d] = reversed(L[:d])
L[d:]=reversed(L[d:])
L[:]=reversed(L[:])
print(L)    