"""
Docstring for Binary Search.Median of Row wise Sorted Matrix

Time Complexity : 
Space Complexity : 

"""
def LowValue(matrix):
    mini = float("inf")
    for i in range(len(matrix)):
        mini = min(mini,matrix[i][0])
    return mini 
def HighValue(matrix):
    maxi = float("-inf")
    for i in range(len(matrix)):
        maxi = max(maxi,matrix[i][len(matrix[0])-1])
    return maxi 

def NumberofElements(matrix,x):
    count = 0
    for i in range(len(matrix)):
        low = 0 
        high = len(matrix[0])-1
        ans = 0
        while(low <= high):
            mid = low + (high-low)//2
            if matrix[i][mid] <= x:
                ans = mid 
                low = mid + 1
            else:
                high = mid - 1
        count += (ans+1) 
    return count 
                
        
def Binary_Search(matrix):
    low = LowValue(matrix)
    high = HighValue(matrix)
    while(low <= high):
        mid = low + (high-low)//2
        if NumberofElements(matrix,mid) <= (len(matrix)*len(matrix[0]))//2:
            low = mid +1  
        else:
            high = mid - 1
    return low 
            
matrix=[[1,5,7,9,11],[2,3,4,9,9],[4,11,14,19,20],[6,10,22,99,100],[7,15,17,24,28]]
print(Binary_Search(matrix))

