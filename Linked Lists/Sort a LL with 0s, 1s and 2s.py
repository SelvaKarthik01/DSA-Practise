"""
Docstring for Linked Lists.Sort a LL with 0s, 1s and 2s

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

def display(head):
    print(head.val,end="") 
    curr= head.next
    while(curr):
        print("->",curr.val,end = "")
        curr = curr.next 
        
def Sort(head):
    dummy_zero= zero = Node(0)
    dummy_one = one = Node(1)
    dummy_two = two = Node(2)
    curr = head 
    while(curr != None):
        if curr.val == 0:
            zero.next = curr 
            zero = curr 
        elif curr.val == 1:
            one.next =curr
            one = curr 
        elif curr.val == 2:
            two.next = curr 
            two = curr 
        curr = curr.next 
    head = dummy_zero.next 
    zero.next = dummy_one.next 
    one.next = dummy_two.next 
    two.next = None # Remember to Complete the Last Two Pointer as None other wise it would point towards the last non-updated one 
    return head  
        
L = [1,2,1,2,0,0]
head = None
for i in range(len(L)):
    head = Insert(head,L[i])
head = Sort(head)
display(head)