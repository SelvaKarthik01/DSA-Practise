# In order to find the ith bit of anumber we can use Bitwise AND Operation for it 
n = int(input("Enter the number :"))
i = int(input("Enter the ith Position : "))
# Create a mask for it at the ith position so we need to pad i-1 zeros on the right so we can left shift i-1 times for this
mask = 1 << (i-1)
n = n & mask
n = n >> (i-1)
print(n)
# If the ith bit is 1 then it will return 1 else it will return 0
