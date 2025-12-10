# We need to set the reverse the ith bit 1->0 or 0->1
n = int(input("Enter the Number : "))
i = int(input("Enter the Value for i : "))
n = n ^ (1<<i)
print(n)