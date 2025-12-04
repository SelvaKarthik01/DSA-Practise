n = int(input("Enter the Number N "))
t = n 
sum = 0
while(t>0):
    sum = sum * 10 + (t%10)
    t = t//10
if sum == n:
    print("True")
else:
    print("False")