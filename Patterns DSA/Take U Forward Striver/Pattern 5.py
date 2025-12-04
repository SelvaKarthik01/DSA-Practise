""" 
*****
****
***
**
*

"""

n = int(input("Enter the Number N : "))
for row in range(n):
    for col in range(n-row,0,-1):
        print("*",end = " ")
    print()