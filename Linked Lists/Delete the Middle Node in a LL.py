"""
Docstring for Linked Lists.Delete the Middle Node in a LL

Time Complexity : O(n)
Space Complexity : O(1)

"""
class Node:
    def __init__(self,val,next=None):
        self.val = val
        self.next = next 
    def __str__(self):
        return f"{self.val}"

def Insert(head,val):
    newnode = Node(val)
    if head == None:
        return newnode 
    else:
        curr = head
        while(curr.next != None):  # Until we reach the Last Node in Linked List  
            curr = curr.next 
        curr.next = newnode 
    return head  

def DeleteMiddleNode(head):
    if head is None or head.next is None:
        return None 
    fast = head 
    slow = head 
    prev = None 
    while(fast is not None and fast.next is not None):
        prev = slow 
        fast = fast.next.next 
        slow = slow.next
    prev.next = slow.next 
    return head  
    

def display(head):
    print(head.val,end="") 
    curr= head.next
    while(curr):
        print("->",curr.val,end = "")
        curr = curr.next 
        
L = [1,2,3,4,5,6,7,8,9,10]
head = None
for i in range(len(L)):
    head = Insert(head,L[i])
head = DeleteMiddleNode(head)
display(head)