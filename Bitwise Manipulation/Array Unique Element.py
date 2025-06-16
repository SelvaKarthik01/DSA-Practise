# All Elements in an Array Appears twice except one find that number 
# We could use the XOR Operation for this because a ^ a = 0 hence all duplicates get cancelled out and get the only unique number from it 
L = eval(input("Enter the List of Numbers : "))
unique = 0 
for i in L:
    unique ^= i
print(unique)