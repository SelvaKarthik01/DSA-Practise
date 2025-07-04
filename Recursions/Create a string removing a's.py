# TO Create  new String after removing all a's from it or any character from it using recursions 
def remove_char(s,input_str,index):
    if index == len(input_str):
        return s
    if input_str[index] != "a":
        s += input_str[index]
    return remove_char(s,input_str,index+1)
input_str = input("Enter the String : ")
print(remove_char("",input_str,0))
        
    