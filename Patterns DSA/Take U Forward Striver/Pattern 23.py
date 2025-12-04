""" 
                      N = 5
          *****     0
         *   *      1
        *   *       2
       *   *        3
      *****         4

"""
n = int(input("Enter the Number N : "))
for row in range(n):
    for col in range(2*n-1):
        if row == 0 :
            if col >= n-1:
                print("*",end ="")
            else:
                print(" ",end = "")
            continue
        if row == n-1 :
            if col <= n-1:
                print("*",end ="")
            else:
                print(" ",end = "")
            continue
            
        elif col == 2*n-2-row or col == n-1-row:
            print("*",end = "")
        else:
            print(" ",end="")
    print()
        