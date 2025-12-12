"""
Docstring for Arrays.Pascals Triangle

1                        Row starts with 0 -> rCc  if it starts with 1 r-1Cc-1
1 1
1 2 1
1 3 3 1
1 4 6 4 1
1 5 10 10 5 1

There could possibly be three problems asked on this 

1) Find the element in the Pascals Triangle at given Row and Columns 
Formula -> row-1 C col-1 

row-1!/(col-1)!*(row-1-col-1)! -> this gives us the elements present at row,col in pascal triangle 

We can Minimise this computation by running it only for few times 
10 C 3 -> 10 * 9 * 8 (reduce 10 by 3 timkes that is r times in nCr)

10/1 * 9/2 * 8/3 -> Computationally Efficient

Very important 
"""
row = int(input("Enter the Row : "))
col = int(input("Enter the Column : "))
res = 1 
for i in range(col-1):
    res = res * (row-1-i)
    res = res // (i+1)
print(res)

""" 
2) We need to print any of the nth row in the pascals triangle 

Lets say we want the 6th Columns we can use the above one run a for loop for col from 1 to 6 and print it using that formula

n = int(input("Enter the Row Number : "))
for col in range(1,n+1):
    res = 1
    for i in range(col-1):
        res = res * (row-1-i)
        res = res //(i+1)
    print(res,end = " ") 
TC -> O(n^2)
SC -> O(1)

Time Complexity : O(n) -> Only one loop through the n
Space Complexity : O(1)
"""
n = int(input("Enter the Row Number : "))
ans = 1
print(ans,end = " ")
for i in range(1,row):
    ans = ans * (row-i)*(1/i)
    print(int(ans),end = " ")
print()
    
""" 
3) Printing the Pascals Triangle 

Given row number n we need to print the Pascals triang;e 
We could take advantage of the previous two sums in solving these 

Time Complexity : O(n^2)
Space Complexity : O(1) 
"""
n = int(input("Enter the Number of Rows : "))
for row in range(1,n+1):
    ans = 1
    print(ans,end= " ")
    for col in range(1,row):
        ans = ans * (row-col)//col
        print(ans,end = " ")
    print()
        
