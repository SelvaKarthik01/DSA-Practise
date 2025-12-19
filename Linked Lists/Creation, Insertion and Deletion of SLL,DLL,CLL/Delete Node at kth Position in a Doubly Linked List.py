"""
Docstring for Linked Lists.Delete Node at kth Position in a Doubly Linked List

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
def Deleteatk(head,k):
    if k == 1:    # What if DLL has only zero or one node 
        if head is None or head.next is None:
            return None 
    count = 1 
    curr = head 
    while(count != k):                    # If k is in between 
        curr = curr.next 
        count += 1
    curr.prev.next = curr.next 
    if curr.next != None:   # What if k is the lastv element in the DLL 
        curr.next.prev = curr.prev 
    return head 
    
L = [1,2,3,4,5,6,7,8,9,10]
head = None
for i in range(len(L)):
    head = Insert(head,L[i])
k = int(input("Enter the Position to be Deleted : "))
head = Deleteatk(head,k)
display_forward(head)
print()
display_backward(head)
    
        