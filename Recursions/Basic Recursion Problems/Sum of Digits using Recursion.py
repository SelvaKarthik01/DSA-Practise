# To Find teh Sum of digits using Recursion 
def sum_of_digits(n):
    if n == 0:
        return 0
    return n % 10 + sum_of_digits(n//10)
n = int(input("Enter the Number : "))
print(sum_of_digits(n))