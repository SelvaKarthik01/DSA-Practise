L = eval(input("Enter the List : "))
max_el = max(L)
xor_expected = 0 
if max_el%4 == 0:
    xor_expected = max_el
elif max_el % 4 == 1:
    xor_expected = 1
elif max_el % 4 == 2:
    xor_expected = max_el + 1 
elif max_el % 4 == 3:
    xor_expected = 0 
xor_real = 0
for i in L:
    xor_real = xor_real ^ i
print(xor_real^xor_expected)
    