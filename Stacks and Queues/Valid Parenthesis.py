s = input("Enter the String : ")
stack = []
for i in s:
    if i == "(" or i == "{" or i == "[":
        stack.append(i)
    else:
        top = stack[-1]
        stack.pop()
        if i == ")" and top == "(":
            continue
        elif i == "}" and top == "{":
            continue 
        elif i == "]" and top == "[":
            continue 
        else:
            print("False")
            break 
else:
    print("True")