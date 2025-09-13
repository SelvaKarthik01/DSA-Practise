n = int(input("Enter the Number : "))
prev2 = 0
prev = 1
for i in range(2,n+1):
    curr = prev2 + prev
    prev2 = prev
    prev = curr 
print(curr)
    