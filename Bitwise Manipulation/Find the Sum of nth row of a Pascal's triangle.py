"""
1
1 1
1 2 1
1 3 3 1
1 4 6 4 1
"""

n = int(input("Enter the Number N : "))

# Formula is 2^n-1 
ans = 1 << n-1
print(ans)
