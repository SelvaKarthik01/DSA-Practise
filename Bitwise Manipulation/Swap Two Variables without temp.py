a = int(input("Enter the Number 1: "))
b = int(input("Enter the Number 2: "))
a = a ^ b 
b = a ^ b 
a = a ^ b 
print(a)
print(b)