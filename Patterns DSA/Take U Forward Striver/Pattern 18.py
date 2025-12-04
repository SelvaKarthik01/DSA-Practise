""" 
     N = 5
E
D E
C D E
B C D E
A B C D E

"""

n = int(input("Enter the Number N : "))
for row in range(n,0,-1):
    for col in range(n-row+1):
        print(chr(ord("A")+row-1+col),end = "")
    print()
        
