jump = eval(input("Enter the Jump Array : "))
def jump_possible(jump):
    max_index = 0
    for i in range(len(jump)):
        if i > max_index:
            return False
        max_index = max(max_index,i+jump[i])
    return True
        
        
        
print("Possible : ",jump_possible(jump))
