"""
Docstring for Numbers.SPF Smallest Prime Factorization

Time Complexity : O(n) -> Creating the Sieve Array + O(nlog(logn)) -> Prime Harmonic Series + O(k) -> k Smallest Prime Numbers 
                 => O(mlog(logn))
Space Complexity : O(n) -> Sieve Array Space 
"""
import math 
def soe(n):
    sieve = [1]*(n+1) # O(n) 
    sieve[0]=sieve[1] = 0 
    for i in range(2,int(math.sqrt(n)+1)): # O(nlog(logn))
        if sieve[i] == 1:
            mul = i 
            while(i*mul <= n):
                if sieve[i*mul] == 1:
                    sieve[i*mul] = i 
                mul += 1
    return sieve 

n = int(input("Enter the Number N : "))
prime_factors = []
sieve = soe(n)
print(f"Smallest Prime Factors of {n} : ",end = " ")
while(sieve[n] != 1):         # O(k)    
    prime_factors.append(sieve[n])
    n = n // sieve[n]
prime_factors.append(n)
print(prime_factors)