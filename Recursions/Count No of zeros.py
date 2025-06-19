# To Count the Number of Zeros in a Number using Recursion
def count_zeros(n):
    if n == 0:
        return 0
    if n %10 == 0 :
        return 1 + count_zeros(n//10)
    else:
        return count_zeros(n//10)
n = int(input("Enter tthe Nuumber : "))
print(count_zeros(n))
