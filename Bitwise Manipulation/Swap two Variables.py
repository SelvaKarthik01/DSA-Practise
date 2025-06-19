# To Swap Two variables without any temporary Variable 
a =int(input("Enter the a : "))
b = int(input("Enter value for b : "))
a = a ^ b
b = a ^ b 
a = a ^ b
print(a)
print(b)