""" 
1             0
0 1           1
1 0 1         2 
0 1 0 1       3
1 0 1 0 1     4

"""

n = int(input("Enter the Number : "))
for row in range(n):
    for col in range(row+1):
        if row%2 == col%2:
            print("1",end = " ")
        else:
            print("0",end= " ")
    print()