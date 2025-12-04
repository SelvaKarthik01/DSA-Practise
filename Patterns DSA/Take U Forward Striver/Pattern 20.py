""" 

                N = 5 [Star,Space, Star]
*        *              [1,8,1]    0
**      **              [2,6,2]    1
***    ***              [3,4,3]    2
****  ****              [4,2,4]    3
**********              [5,0,5]    4
****  ****              [4,2,4]    5
***    ***              [3,4,3]    6
**      **              [2,6,2]    7
*        *              [1,8,1]    8

"""

n = int(input("Enter the Number N : "))
for row in range(2*n-1):
    if row >= n:
         row = 2*n-row-2
    for col in range(row+1):
        print("*",end ="")
    for col in range(2*n-(2*(row+1))):
        print(" ",end ="")
    for col in range(row+1):
        print("*",end = "")
    print()