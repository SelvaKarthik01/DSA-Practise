"""
1 2 3 4 5
1 2 3 4 
1 2 3 
1 2 
1

"""

n = int(input("Enter the value for N : "))
for row in range(n):
    for col in range(1,n-row+1):
        print(col,end = " ")
    print()