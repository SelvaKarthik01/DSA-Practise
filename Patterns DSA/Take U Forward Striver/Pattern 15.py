""" 
ABCDE
ABCD
ABC
AB
A

"""

n = int(input("Enter the Number : "))
for row in range(n,0,-1):
    for col in range(65,65+row):
        print(chr(col),end = "")
    print()
    