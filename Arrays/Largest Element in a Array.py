arr = eval(input("Enter the List : "))
largest = arr[0]
for i in arr:
    if i > largest:
        largest = i 
print(largest)