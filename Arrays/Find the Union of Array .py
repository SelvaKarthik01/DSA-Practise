a = eval(input("Enter the List 1 : "))
b = eval(input("Enter the List 2 : "))
n1 = len(a)
n2 = len(b)
int = []
i =0
j = 0 
while(i < n1 and j < n2):
    if a[i] == b[j]:
        if len(int) == 0 :
            int.append(a[i])
        elif len(int) != 0 and int[-1] != a[i]:
            int.append(a[i]) 
        i +=1 
        j +=1
    elif a[i] != b[j] and a[i] < b[j]:
        i += 1
    elif a[i] != b[j] and b[j] < a[i]:
        j +=1
print(int)

            