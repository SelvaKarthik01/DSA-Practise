"""
Docstring for Linked Lists.Insert at the Kth Position in a Doubly Linked List

Time Complexity : O(k)
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
    if head is None:
        print(None)
        return 
    print(head.val,end = "")
    curr = head
    curr = curr.next
    while(curr):
        print("->",curr.val,end = "")
        curr = curr.next 
        
def display_backward(head):
    if head == None :
        print(None)
        return 
    curr = head 
    while(curr.next != None):
        curr = curr.next
    print(curr.val,end="")
    curr= curr.prev
    while(curr):
        print("<-",curr.val,end="")
        curr = curr.prev
        
def Insertatk(head,val,k):
    newnode = Node(val)
    if k == 1:
        newnode.next = head 
        head.prev = newnode 
        return newnode 
    curr = head 
    count = 1
    while(count != k):
        curr = curr.next
        count += 1
    newnode.prev = curr.prev 
    newnode.next = curr 
    curr.prev.next = newnode 
    curr.prev = newnode 
    return head 

L = [1,2,3,4,5,6,7,8,9,10]
head = None
for i in range(len(L)):
    head = Insert(head,L[i])
val = int(input("Enter the Value to be Added : "))
k = int(input("Enter the Positon to be Inserted : "))
head = Insertatk(head,val,k)
display_forward(head)
print()
display_backward(head)
    
        