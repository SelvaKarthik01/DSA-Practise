stack = eval(input("Enter the Stack Elements : "))
def add_bottom(el,stack):
    if (not stack):
        stack.append(el)
        return 
    rest = stack.pop()
    add_bottom(el,stack)
    stack.append(rest)
def recursion(stack):
    if (not stack):
        return 
    el = stack.pop()
    recursion(stack)
    add_bottom(el,stack)
recursion(stack)
print(stack)
        