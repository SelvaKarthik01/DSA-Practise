""" 
1 2 3 4 5 6 7            N = 4

4 4 4 4 4 4 4       1      # Find the Min distance of the element around all four corners and Subract from n
4 3 3 3 3 3 4       2
4 3 2 2 2 3 4       3
4 3 2 1 2 3 4       4
4 3 2 2 2 3 4       5
4 3 3 3 3 3 4       6
4 4 4 4 4 4 4       7


"""

n = int(input("Enter the Number N : "))
for row in range(2*n-1):
    for col in range(2*n-1):
        print(n-min(row,col,(2*n-2)-row,(2*n-2)-col),end =" ")
    print()