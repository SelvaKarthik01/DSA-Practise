""" 
        N = 4 [Space, Letter, SPace]
   A        1  [3,A,3]
  ABA       2  [2,AB A,2]
 ABCBA      3  [1,ABC BA,1]
ABCDCBA     4  [0,ABCD CBA,0]

"""

n = int(input("Enter the Number N : "))
for row in range(n):
    for col in range(n-row):
        print(" ",end = "")
    for col in range(2*row+1):
        if col > row:
            col = 2*row-col
        print(chr(ord("A")+col),end="")
    print()