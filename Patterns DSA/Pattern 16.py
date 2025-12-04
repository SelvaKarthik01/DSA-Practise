""" 
A
BB
CCC
DDDD
EEEEE

"""

n = int(input("Enter the Number N : "))
for row in range(n):
    for col in range(row+1):
        print(chr(ord("A")+row),end = "")
    print()
    
    
        