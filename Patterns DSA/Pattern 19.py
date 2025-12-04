""" 

            N = 5 
**********          [5,0,5]     0       
****  ****          [4,2,4]     1
***    ***          [3,4,3]     2
**      **          [2,6,2]     3
*        *          [1,8,1]     4
*        *          [1,8,1]     5
**      **          [2,6,2]     6
***    ***          [3,4,3]     7
****  ****          [4,2,4]     8
**********          [5,0,5]     9

"""

n = int(input("Enter the Number N : "))
for row in range(2*n):
    if row >= n:
        row = n-(row%n+1)
    for col in range(n-row):
        print("*",end = "")
    for col in range(2*row):
        print(" ",end = "")
    for col in range(n-row):
        print("*",end = "")
    print()
    