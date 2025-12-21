"""
Docstring for Linked Lists.Find Pairs with given Sum in DLL

Sorted DLL 

Time Complexity : O(n) for finding the last element + O(n) for finding the Pairs 
                  Total -> O(n) + O(n) -> O(n)
Space Complexity : O(1) -> Auxiliary Space : O(n) for stroing the Pairs

"""
class Node:
    def __init__(self,val,next=None,prev=None):
        self.val = val 
        self.next = next 
        self.prev = prev
    def __str__(self):
        return f"{self.val}"

def Insert(head,val):
    newnode = Node(val)
    if head == None:
        return newnode 
    curr = head 
    while(curr.next != None):
        curr = curr.next 
    newnode.prev = curr 
    curr.next = newnode
    return  head 

def display_forward(head):
    print(head.val,end = "")
    curr = head
    curr = curr.next
    while(curr):
        print("->",curr.val,end = "")
        curr = curr.next 
        
def display_backward(head):
    curr = head 
    while(curr.next != None):
        curr = curr.next
    print(curr.val,end="")
    curr= curr.prev
    while(curr):
        print("<-",curr.val,end="")
        curr = curr.prev
        
def findPairs(head,k):
    ans = []
    left = head 
    right = head 
    while(right.next is not None):
        right = right.next 
    while(left != right and left.prev != right):
        if left.val + right.val == k:
            ans.append((left.val,right.val))
            left = left.next 
            right = right.prev 
        if left.val + right.val > k:
            right = right.prev 
        if left.val + right.val < k:
            left = left.next 
    return ans 
            
            
L = [1,2,3,4,5,6,7,8,9,10]
head = None
for i in range(len(L)):
    head = Insert(head,L[i])
k = int(input("Enter the Target Sum : "))
ans = findPairs(head,k)
print(ans)
display_forward(head)
print()
display_backward(head)