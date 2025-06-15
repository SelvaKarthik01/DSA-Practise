"""
*
**
***
****
*****
****
***
**
*
"""

n = int(input())
for i in range(2*n):
    if i <= n :
        col = i
    else:
        col = n - (i%n)
    for j in range(col):
        print("*",end = "")
    print()
    
