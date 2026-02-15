# Find out the Prime Numbers uptil n 
#Seive basically removes all the fatcors of the prime numbers instead of checking it again and again to reduce the time complexity 
#Seive of Erasthumus
"""
Docstring for Numbers.Seive of Eratosthenes - Prime numbers

Time Complexity : O(n) -> for Creating the sieve array + O(Nlog(logN)) -> Prime Harmonic Series + O(n) -> For Printing
                       -> O(Nlog(logn))
Space Complexity : O(n) -> for the Sieve Array 
"""
import math 

def soe(n):
    sieve = [1]*(n+1) #O(n)
    sieve[0]=sieve[1] = 0 
    for i in range(2,int(math.sqrt(n)+1)): #O(nlog(logn))
        if sieve[i] == 0:
            continue 
        else:
            mul = i  # Always start from i * i because 5x2 5x3 5x4 all would be marked 5x5 is where we need to actually start for every i
            while(i*mul <= n):
                sieve[i*mul] = 0 
                mul += 1
    return sieve 


n = int(input("Enter the Number N : "))
sieve = soe(n)
print(sieve)
print("Number of Primes numbers till N : ",sum(sieve[2:])) #O(n)
    
    

            