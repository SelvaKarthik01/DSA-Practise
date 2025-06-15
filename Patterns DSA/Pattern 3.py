"""
1
1 2
1 2 3
1 2 3 4
1 2 3 4 5
"""

n = int(input())
for i in range(n):
    for j in range(1,i+2):
        print(j,end = " ")
    print()
    
