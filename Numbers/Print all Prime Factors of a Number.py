"""
Docstring for Numbers.Print all Prime Factors of a Number

Time Complexity : O(sqrt(n)*logn)
Space Complexity : O(logn) # The PRoduct first n prime numbers grows very fast 
"""
import math
def prime_factors(n):
    L = []
    for i in range(2,int(math.sqrt(n)+1)): # O(sqrt(n))
        if n % i == 0:
            L.append(i)
            while(n%i==0): # O(logn)
                n = n // i 
    if n != 1:
        L.append(n)
    return L 

n = int(input("Enter the Value for N : "))
print(prime_factors(n))