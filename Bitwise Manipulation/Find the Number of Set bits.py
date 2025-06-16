# To find the Number of 1s in a binary number for a Number n
n = int(input("Enter the Number : "))
n1 = n
count = 0 
while(n != 0):
    rmb = n & -n
    n = n - rmb
    count += 1
print(count)

#Another Solution is Right Shift it until we get Zero 
n = n1
count = 0 
while(n != 0 ):
    if n & 1:
        count += 1
    n >>= 1 
print(count)
    