# To Find the Product fo digits using Recurisions
def product_digit(n):
    if n == 0 :
        return 1
    return n % 10 * product_digit(n//10)
n = int(input("Enter the Number : "))
print(product_digit(n))