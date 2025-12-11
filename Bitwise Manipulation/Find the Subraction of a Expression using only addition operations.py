a = int(input("Enter the Number 1 : "))
b = int(input("Enter the Number 2 : "))
# ans = a + (-b)
ans = a + ((~b)+1) # 2's Complement 
print(ans)