# Find a Number is Power of 2 or not using Bitwise Operation
# A number is a power of 2 if it has only one bit set in its binary representation.
# Example 2 = 10
# 4 - 100
# 8 - 1000
n = int(input("Enter the number: "))
temp = n & -n
temp = n ^ temp # or temp = n - temp
if temp == 0 :
    print("It is a Power of 2 ")
else:
    print("Not a Power of 2")

