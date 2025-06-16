# We need to reset that is set the ith bit to 0
n = int(input("Enter the Number : "))
i = int(input("Enter the Position : "))
mask = 1 << (i-1)
mask = ~mask

n = n & mask
print(n)