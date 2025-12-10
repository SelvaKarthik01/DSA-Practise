n = int(input("Enter the Number : "))

# 16-> 10000
# 15-> 01111
# And operation of both will set the right most set bit to 0 
n = n & (n-1)
print(n)