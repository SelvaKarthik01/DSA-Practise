"""
Docstring for Numbers.Armstrong Number

Amstrong Number - Extract each Digit and find the Number of Digits Power if the summation equal to the original Number it is a Amstrong Number 

Time Complexity : O(log(n))
Space Complexity : O(1)

"""
import math
def amstrong_number(num):
    n = num
    num_digits = 1
    if n != 0:
        num_digits = int(math.log(n,10)+1)
    sum = 0 
    while(n > 0):
        last_digit = n % 10 
        sum = sum  + (last_digit**num_digits)
        n = n // 10 
    if sum == num:
        return True 
    else:
        return False 
n = int(input("Enter the Number N : "))
print(amstrong_number(n))
        