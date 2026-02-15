"""
Docstring for Numbers.Digits of a Number

To Print the Number of Digits using Extraction og Digits Concept 

Time Complexity : O(log(n))
Space Complexity : O(1)

"""

n = int(input("Enter the Number N : "))
t=n
count = 0 
while(n>0):
    count += 1
    n = n //10 # Dividing by 10 each step so log base n is the TC 
print(count)
import math 
print(int(math.log(t,10)+1)) # TC -> O(logn)