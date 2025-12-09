# Inside a Main function the array max storing is 10^6 elements
# Outside the main as a global variable the array max elements is 10^7 elements

L = eval(input("Enter the List : "))
n = int(input("Enter the Number : "))
hash = dict()
for i in L:
    hash[i] = hash.get(i,0)+1
print(hash.get(n,0))