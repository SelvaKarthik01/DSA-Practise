L = eval(input("Enter the List : "))
L.sort()
last_smallest = L[0]
count = 1
largest = 1
for i in range(1,len(L)):
    if L[i]-1 == last_smallest:
        count += 1
        last_smallest = L[i]
    if L[i]-1 == last_smallest:
        last_smallest = L[i]
        count = 1
    largest = max(count,largest)
print(largest)        