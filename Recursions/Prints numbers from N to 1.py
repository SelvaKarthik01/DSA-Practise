# To Print Numbers from n to 1 using recursions 

def print_num(n):
    if n == 0:
        return 
    print_num(n-1)
    print(n,end = " ")
    
def print_num_rev(n):
    if n == 0 :
        return
    print(n,end = " ")
    print_num_rev(n-1) 
    
     
n = int(input("Enter the Number N :"))
print_num(n)
print_num_rev(n)