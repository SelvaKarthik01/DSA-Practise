n = int(input("Enter the Number : "))
i = int(input("Enter the ith Position : "))
mask = 1 << (i-1)
n = n | mask
print(n)