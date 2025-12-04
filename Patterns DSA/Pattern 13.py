"""  
1
2 3
4 5 6 
7 8 9 10
11 12 13 14 15

"""
count = 1
n = int(input("Enter the Number : "))
for row in range(1,n+1):
    for col in range(row):
        print(count,end = " ")
        count += 1
    print()