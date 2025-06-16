# To find the right most set bit of a number n 
# n = 1 0 1 1 0 1 0 0  here 1 is the the right most how to find that 
# general Fomrula n = a 1 b where b is always zero 
# -n = a complement 1 b 
# vif we try to AND both of them we will get the right most set bit
n = int(input("Enter the Number : "))
n = n & -n
print(n)