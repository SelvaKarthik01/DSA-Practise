greed = eval(input("Enter the Number of Cookies needed by Each children : "))
cookies = eval(input("Enter the Available Cookies : "))
greed.sort()
cookies.sort()
l = r = 0
count=0
while(l < len(cookies)):
    if cookies[l] >= greed[r]:
        count += 1
        l += 1
        r += 1
    else:
        l+=1 
print("No. of Childrens Satisfied or Assigned Cookies with : ",count)
    
