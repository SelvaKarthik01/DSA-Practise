""" 
1
22
333
4444
55555

"""

n = int(input("Enter the Value for N : "))
for row in range(1,n+1):
    for col in range(row):
        print(row,end = " ")
    print()
        