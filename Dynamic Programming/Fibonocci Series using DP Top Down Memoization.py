n = int(input("Enter the Number : "))
dp = [-1]*(n+1)
def fibo(n,dp):
    if n <= 1 :
        return n
    if dp[n] != -1:
        return dp[n]
    else:
        dp[n] = fibo(n-1,dp)+fibo(n-2,dp)
        return dp[n]
print(fibo(n,dp))
    