L = eval(input("Enter the List : "))
i=0
j = i +1
while(j < len(L)):
    if L[i] < 0 and i % 2 == 0:
        while(j < len(L) and L[j] < 0):
            j += 1
        if j < len(L):
            L[i],L[j] = L[j],L[i]
    elif L[i] > 0 and i % 2 == 1:
        while(j < len(L) and L[j] > 0 ):
            j += 1
        if j < len(L):
            L[i],L[j] = L[j],L[i]  
    i += 1
    j += 1
print(L)