# TO Find the Factorial of a Number using Recursion 

def factorial_num(n):
    if n == 1:
        return 1
    return n * factorial_num(n-1)
n = int(input("Enter the Number : "))
print(factorial_num(n))