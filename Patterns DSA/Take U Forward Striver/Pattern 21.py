""" 
          N = 5
* * * *    # Fill only the Boundries thats the clue 
*     *
*     *
*     *
* * * *

"""
n = int(input("Enter the Number N : "))
for row in range(n):
    for col in range(n):
        if row == 0 or row == n-1 or col == 0 or col == n-1:
            print("*",end = " ")
        else:
            print(" ",end = " ")
    print()