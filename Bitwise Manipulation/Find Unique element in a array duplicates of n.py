# Given a array of integers where integers have n duplicates and one unique element we need to find that unique element in that array
L = eval(input("Enter the List fo numbers : "))
n = int(input("How many Numbers are duplicated : "))
largest = max(L)
# Create a mask for the largest number in the array
stopper = 1 << (largest.bit_length() )
mask = 1
sum = 0
ans = []
while(mask != stopper):
    for i in L:
        sum = 0
        if (mask & i) != 0:
            sum += 1
    ans.append(str(sum%n))
    mask <<= 1
    

ref = ''.join(ans)[::-1]
print(int(ref,2))




    
    