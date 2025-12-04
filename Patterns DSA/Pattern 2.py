""" 
*
**
***
****
*****
"""

n = int(input("Enter the Number N : "))
for row in range(n):
    for col in range(row+1):
        print("*",end = " ")
    print()