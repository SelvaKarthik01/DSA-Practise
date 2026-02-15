"""
Docstring for Numbers.Reverse a Number

To Find the Reverse of a Number using of Extratcion of Digits Concept 

Time Complexity : O(logn)
Space Complexity : O(1)

"""

def reverse(n):
    sum = 0
    t = n 
    while(t > 0):
        last_digit = t % 10 
        sum = (sum * 10)+ last_digit 
        t = t // 10 
    return sum 
n = int(input("Enter the Number N : "))
print(reverse(n))