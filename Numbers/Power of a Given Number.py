a = int(input("Enter the Number for a : "))
b = int(input("Enter the Number for b : "))
flag = 0
if b < 0:
    b = b * -1
    flag = 1
ans = 1
while(b!=0):
    if b & 1 == 1:
        ans *= a 
        b -= 1
    else:
        a = a ** 2
        b = b //2
if flag == 1:
    print(1/ans)
else:
    print(ans)