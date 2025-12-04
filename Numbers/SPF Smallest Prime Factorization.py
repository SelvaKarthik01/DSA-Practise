n = int(input("Enter the Number : "))
seive = [0]*(n+1)
def soe(seive,n):
    for i in range(2,n+1):
        a = 1
        while(i*a <= n):
            if seive[i*a] == 0:
                seive[i*a] = i
            a += 1
    
ans = []
soe(seive,n)
while(n!=1):
    ans.append(seive[n])
    n = n // seive[n]
print(ans)
