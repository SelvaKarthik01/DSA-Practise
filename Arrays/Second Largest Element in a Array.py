arr = eval(input("Enter the List : "))
largest = arr[0]
slargest = float("-inf")
for i in range(len(arr)):
    if arr[i] > largest:
        slargest = largestlargest = arr[i]
    if arr[i] < largest and arr[i] > slargest:
        slargest = arr[i]
print(slargest)
# Time Complexity O(n)

