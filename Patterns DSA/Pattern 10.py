"""
            N = 5
*       0
**      1
***     2
****    3   
*****   4
****    5
***     6
**      7
*       8

"""

n = int(input("Enter the Number N : "))

for row in range(2*n-1):
    if row >= n:
        row = 2*n-row -2 
    for col in range(row+1):
        print("*",end = " ")
    print()
              
        
    