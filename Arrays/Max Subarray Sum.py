L = eval(input("Enter the List : "))
max = float("-inf")
sum = 0 
hold = 0
for i in range(len(L)):
    sum += L[i]
    if sum < 0:
        sum = 0
        continue
    if sum > max:
        max = sum
if max < 0:
    max = -1
        
print(max)
        
    