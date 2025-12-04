""" 
          [Space,Star,space]  N = 4
   *      [3,1,3]    0
  ***     [2,3,2]    1
 *****    [1,5,1]    2 
*******   [0,7,0]    3
 *****    [1,5,1]    4
  ***     [2,3,2]    5
   *      [3,1,3]    6

"""

n = int(input("Enter the Number N : "))

for row in range(2*n-1):
    if row >= n:
        row = 2*n - row - 2
        
    for col in range(n-row-1):
        print(" ",end = "")
    for col in range(2*row+1):
        print("*",end = "")
    for col in range(n-row-1):
        print(" ",end = "")
    print()