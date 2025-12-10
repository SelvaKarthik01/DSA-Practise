n = int(input("Enter the Number : "))
i = int(input("Enter the value for i : "))
if n & (1 << i) : # Left Shift 
    print("True")
else:
    print("False")

while(i != 0): # Using Right Shift
    n = n >>1
    i -= 1
if n & 1:
    print("True")
else:
    print("False")