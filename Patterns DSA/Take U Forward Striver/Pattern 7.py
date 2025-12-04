"""         [Space, Star, Space]
    *        [4,1,4]
   ***       [3,3,3]
  *****      [2,5,2]
 *******     [1,7,1]
*********    [0,9,0]

"""
n = int(input("Enter the Value for N : "))
for row in range(n):
    for col in range(n-row-1,0,-1):
        print(" ",end = " ")
    for col in range(row*2+1):
        print("*",end = " ")
    for col in range(n-row-1,0,-1):
        print(" ",end = "")
    print()