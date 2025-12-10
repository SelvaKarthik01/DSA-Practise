n = int(input("Enter the Number : "))
goal = int(input("Enter the Goal : "))
# Xor operation will tell us which bits are different by giving us 1 in the ans
ans = n ^ goal 
count = 0
while(ans !=0):
    ans = ans & (ans-1)
    count += 1
print(count)