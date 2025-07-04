arr = eval(input("Enter the Array : "))
d = int(input("Enter the D Value : "))
d = d % len(arr)
left = arr[:d]
right = arr[d+1:]
right.extend(left)
print(right)