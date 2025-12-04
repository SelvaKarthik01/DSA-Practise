""" 
    N = 5
A
AB
ABC
ABCD
ABCDE

"""

n = int(input("Enter the Number N : "))
for row in range(1,n+1):
    for col in range(65,65+row):
        print(chr(col),end ="")
    print()