"""
Docstring for Numbers.Power of a Given Number

Time Complexity : O(logn)
Space Complexity : O(1)
"""

a = eval(input("Enter the Base Number : "))
b = int(input("Enter the Power Raised to : "))

flag = 0
if b < 0 :
    flag = 1 
    b = b * -1 
ans = 1 
while(b != 0):
    if b % 2 == 0:
        a = a * a 
        b = b//2       # O(logn)
    else:
        ans = ans * a 
        b -= 1

if flag:
    print(1/ans)
else:
    print(ans)
    