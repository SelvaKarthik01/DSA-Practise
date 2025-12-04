n = int(input("Enter the Number N : "))
t = n 
sum = 0 
num_digits = len(str(n)) # or int(math.log(n,10)+1)
while(t>0):
    sum = sum + (t%10)**num_digits
    t = t//10

if sum == n:
    print("true")
else:
    print("false")