# TO Find a Number is Even or Odd using Bitwise Operation
# 8 = 1000 last digit is 0 
# 7 = 111 last digit is 1
# This code checks if a number is even or odd using bitwise operation
n = int(input("Enter the Number : "))
if n & 1 == 0 :
    print("Even Number ")
else:
    print("Odd Number")
    