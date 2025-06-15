"""
         *
        **
       ***
      ****
     *****
"""

n = int(input())
for i in range(n,0,-1):
    space = n - i
    print(" "*space,end = "")
    for j in range(i):
        print("*",end = "")
    
    print()
    
