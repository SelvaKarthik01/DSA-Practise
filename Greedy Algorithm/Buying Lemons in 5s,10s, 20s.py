bills = eval(input("Enter the Currency Note for each Customer to buy Lemons : "))
def possible_transaction(bills):
    five,ten = 0,0
    for i in bills:
        if i == 5:
            five += 1
        elif i == 10 and five !=0:
            five -= 1
            ten += 1
        elif i == 10 and five == 0:
            return False 
        else:
            if five !=0 and ten !=0:
                five-=1
                ten -= 1
            elif five >= 3:
                five -= 3
            else:
                return False
    return True     
print("Given Transactrion : ",possible_transaction(bills))
            