""" 
             [Space, Star, Space]
*********    [0,9,0]
 *******     [1,7,1]
  *****      [2,5,2]
   ***       [3,3,3]
    *        [4,1,4]

"""
n = int(input("Enter the Number N : "))
for row in range(n-1,-1,-1):
    for col in range(n-row-1,0,-1):
        print(" ",end = " ")
    for col in range(2*row+1,0,-1):
        print("*",end = " ")
    for col in range(n-row-1,0,-1):
        print(" ",end = " ")
    print()