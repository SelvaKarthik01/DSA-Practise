""" 
*****
****
***
**
*
Using recursion

"""

def Triangle1(row,column):
    if row == 0:
        return
    if column < row:
        print("*",end = " ")
        Triangle1(row,column+1)
    else:
        print()
        Triangle1(row-1,0)
row = int(input("Enter the N : "))
Triangle1(row,0)