
row = int(input("Enter the Row : "))
col = int(input("Enter the Column : "))
def factorial(n):
    if n==0 or n == 1:
        return 1
    return n * factorial(n-1)
ans = factorial(row-1)/(factorial(row-1 - col-1)* factorial(col-1))
print(ans)