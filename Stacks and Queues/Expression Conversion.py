# Infix to Postfix expression conversion 
s = input("Enter the Infix Expression : ")
stack = []
priority = {"^":3,"/":2,"*":2,"+":1,"-":1,"(":0,")":0}
ans = ""
for i in s:
    if i.isalnum():
        ans+= i
    elif i in "^/*+-()":
        current_prior = priority[i]
        if not stack:
            stack.append(i)
            continue
        top = stack[-1]
        if current_prior >= priority[top]:
            stack.append(i)
        else:
            stack.pop()
            ans += top 
            stack.append(i) 
    print(stack)
while(stack):
    ans += stack.pop()
print(ans)


# Infix to Postfix 

# Step 1 : Reverse the Infix Expression 
# Step 2 : Infix 2 Postfix Expression COnversion as same as before
# Step 3 : Reverse the Answer 

s = input("Enter the Infix Expression : ")
s = s[::-1]
print(s)
s=s.replace("(","#")
s=s.replace(")","(")
s=s.replace("#",")")

print(s)
stack = []
priority = {"^":3,"/":2,"*":2,"+":1,"-":1,"(":0,")":0}
ans = ""
for i in s:
    if i.isalnum():
        ans+= i
    elif i in "^/*+-()":
        current_prior = priority[i]
        if not stack:
            stack.append(i)
            continue
        top = stack[-1]
        if current_prior >= priority[top]:
            stack.append(i)
        else:
            stack.pop()
            ans += top 
            stack.append(i) 
    print(stack)
while(stack):
    ans += stack.pop()
ans = ans[::-1]
print(ans)


# Postfix to Infix Expression Conversion 

# Second Operator First in Stack
s = input("Enter the Postfix Expression : ")
stack = []
for i in s:
    if i.isalnum():
        stack.append(i)
    elif i in "+-*/^":
        first = stack.pop()
        second = stack.pop()
        new = "("+str(second)+str(i)+str(first)+")"
        stack.append(new)
print(stack[-1])          
        
# Prefix to Infix Expression Conversion 
#Traverse from Last to First in Prefix Expression

#First Operator Second  in Stack

s = input("Enter the Prefix Expression : ")
stack = []
for i in range(len(s)-1,-1,-1):
    print(s[i])
    if s[i].isalnum():
        stack.append(s[i])
    elif s[i] in "+-*/^":
        first = stack.pop()
        second = stack.pop()
        new = "("+str(first)+str(s[i])+str(second)+")"
        stack.append(new)
print(stack)
        
    