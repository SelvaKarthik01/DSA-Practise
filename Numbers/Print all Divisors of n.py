"""
Docstring for Numbers.Print all Divisors of n

One approach run a loop from 1 to n and find the % == 0 and include this 
TC -> O(n)
SC -> O(1)

Time Compleixty : O(sqrt(n)) + O(nlogn)
Space Complexity : O(n) Auxiliary Space 

"""
import math 
def all_divisors(n):
    divisors = []
    for i in range(1,int(math.sqrt(n)+1)): # O(sqrt(n))  Better to use While Loop for i * i to avoid Floating point precision and tiny Performance Difference 
        if n % i == 0:
            divisors.append(i)
            if n // i != i:
                divisors.append(n//i)
    return divisors
n = int(input("Enter the Number N : "))
print(sorted(all_divisors(n))) # O(nlogn)
            