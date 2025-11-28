L = eval(input("Enter the List : "))
d = int(input("Enter the Value of D : "))
L[:d]=reversed(L[:d])
L[d:]=reversed(L[d:])
L=L[::-1]
print(L)