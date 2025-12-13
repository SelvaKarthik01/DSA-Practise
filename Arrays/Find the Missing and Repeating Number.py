"""
Docstring for Arrays.Find the Missing and Repeating Number

Another Approach is to iterate through the array with a count if count is present cehck its count in array ban dif its two thats
the repeating elements and if count not present in array thats the missing elements 
TC-> O(n^2) taking one elements and looking for other occurences for count
SC->O(1)

Another Approach create a dictionary with 1 to n having count as zero go thourgh the Array and increamenet the count 
Find the element with count as 2 and zero using key value pairs 
TC-> O(n) for creating the hashmap + O(n) for incrementing the count + O(n) finding out count as 0 and count 1
     Total -> O(n)+O(n)+O(n) -> O(3n) -> O(n)
SC -> O(n) for storing the elements in Hashmap 

Another Approach would be Find the sum of all elemnst in array and find the sum of n natural numbers 
sum - sum of n = x- y one equation 
simialrly do it for squarres we get x^2-y^2 = (x+y)*(x-y) use x-y in the quation find x+y and Solve Linear Equaltions using Two vairables 
TC -> O(n) for finding the Sum and Square Sum 
Sc -> O(1)

Time Complexity : O(n) for finding the xor of the Elements in Array + O(n) for finding the Elements to categories + O(n) for 1 to n categories
                  Total -> O(n) + O(n) + O(n) -> O(3n)-> O(n)
Space Complexity : O(1) just xor variables 

"""
n = int(input("Enter the Number N : "))
L = eval(input("Enter the List : "))
if n % 4 == 0:
    xor_n = n 
elif n % 4 == 1:
    xor_n = 1 
elif n % 4 == 2:
    xor_n = n + 1
elif n % 4 == 3:
    xor_n = 0 

xor = 0 
for i in range(len(L)):
    xor ^= L[i]
xor_final = xor ^ xor_n 

clear_bit = xor_final&(xor_final-1)
right_set_bit = clear_bit ^ xor_final
 
b1 = 0 
b2 = 0 
for i in range(len(L)):
    if (L[i] & right_set_bit):
        b1 ^= L[i]
    else:
        b2 ^= L[i]
for i in range(1,n+1):
    if (i & right_set_bit):
        b1 ^= i 
    else:
        b2 ^= i 
print(b1)
print(b2)
        
    