# To Check if a number is a palindorme or not using recursion 
import math
def palindrome(n,s,e):
    if n == 0:
        return True
    if e != s :
        return False
    n = (n//10)%10**(int(math.log(n,10)))
    palindrome(n,n//10**(int(math.log(n,10))),n%10)
n = int(input("Enter the Number : "))
print(palindrome(n,n//10**(int(math.log(n,10))),n%10))