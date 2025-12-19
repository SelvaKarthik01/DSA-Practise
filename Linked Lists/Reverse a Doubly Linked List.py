"""
Docstring for Linked Lists.Reverse a Doubly Linked List

Another Approach is to chnaage the val in the Node using LIFO Stack 
TC -> O(n) for storing the .val in Stack + O(n) for replacing the values 
SC -> O(n) stack space 

Time Complexity : O(n)
Space Complexity : O(1)

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
        
def ReverseDLL(head):
    curr = head 
    if head is None or head.next == None:
        return head 
    temp = curr.next 
    curr.next,curr.prev = curr.prev,curr.next
    curr = temp  
    while(curr.next != None):
        temp = curr.next
        curr.next,curr.prev = curr.prev,curr.next
        curr = temp 
    curr.next,curr.prev = curr.prev,curr.next
    return curr  
    

L = [1,2,3,4,5,6,7,8,9,10]
head = None
for i in range(len(L)):
    head = Insert(head,L[i])
head = ReverseDLL(head)
display_forward(head)
print()
display_backward(head)
    
        