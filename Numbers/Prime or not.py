"""
Docstring for Numbers.Prime or not

Time Complexity : O(sqrt(n))
Space Complexity : O(1)
"""

import math
n = int(input("Enter the Number : "))
for i in range(2,int(math.sqrt(n))+1):
    if n % i == 0 :
        print("Not a Prime")
        break
else:
    print("Prime")