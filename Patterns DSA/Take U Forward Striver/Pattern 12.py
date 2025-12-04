""" 
            N = 4   [Number , Space ,  Number]
1      1      1     [row,2*n-2,row]
12    21      2     
123  321      3 
12344321      4

"""

n = int(input("Enter the Value for N : "))
for row in range(1,n+1):
    for col in range(1,row+1):
        print(col,end = '')
    for col in range(2*n-(2*row)):
        print(" ",end = "")
    for col in range(row,0,-1):
        print(col,end = "")
    print()