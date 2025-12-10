L = eval(input("Enter the List : "))
# The Array consists of all element repeated twice except two distinct elements we need to find the distinct elements 
xor = 0 
for i in L:
    xor = xor ^ i

right_set_bit = ((xor & (xor-1))^xor)

xor1 = 0
xor2=0
for i in L:
    if i & right_set_bit:
        xor1 ^= i
    else:
        xor2 ^= i
print(xor1,xor2)


    