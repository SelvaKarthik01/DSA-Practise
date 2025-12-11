n = int(input("Enter the Number n : "))

sieve = [1]*(n+1)
sieve[0]=0
sieve[1] = 0
def soe(sieve,r):
    for i in range(2,r+1):
        count = 2 
        while(i*count <= r):
            sieve[i*count] = 0
            count += 1

soe(sieve,n)
print(sieve)
print(sum(sieve))
    