"""
         *
        **
       ***
      ****
     *****
"""

n = int(input())
for i in range(1,n+1):
    space = n - i
    print(" "*space,end = "")
    for j in range(i):
        print("*",end = "")
    print()
    
