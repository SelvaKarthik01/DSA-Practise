"""
Docstring for Numbers.Print all Prime Factors of a Number

Time Complexity : O(sqrt(n))
Space Complexity : O(n) Auxiliary Space 

"""
import math 
def PrimeFactors(n):
    L = [1]
    for i in range(2,int(math.sqrt(n)+1)):
        if n % i == 0:
            L.append(i)
            while(n%i == 0):
                n = n // i 
    if n != 1:
        L.append(n)
    return L
    
n = int(input("Enter the Number N : "))

print(PrimeFactors(n))