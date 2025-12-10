n = int(input("Enter the Number : "))
temp = n
count = 0
while (n != 0):
    n = n & (n-1)
    count += 1
print(count)

# Another way is to right shift and and operation with 1 to check if 1 or 0 and then right shift by 1 
count = 0
n = temp
while(n != 0):
    if (n & 1) == 1:
        count += 1
    n = n >> 1
print(count)



