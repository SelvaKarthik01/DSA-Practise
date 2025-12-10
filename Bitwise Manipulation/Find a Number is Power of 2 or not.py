# Find a Number is Power of 2 or not using Bitwise Operation
# A number is a power of 2 if it has only one bit set in its binary representation.
# Example 2 = 10
# 4 - 100
# 8 - 1000
n = int(input("Enter the number: "))

if n & (n-1):
    print("It is not a Power of 2 ")
else:
    print("It is a Power of 2")

