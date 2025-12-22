"""
Docstring for Linked Lists.Flatten a Linked List

Time Complexity : O(n) for horizontal Depth * O(m+m) for child nodes Depth 
                  Total -> O(n*2m)
Space Complexity : O(1) Auxiliary Space Recrusive Stack O(n)
"""
class Node:
    def __init__(self,val,next=None,child = None):
        self.val = val
        self.next = next 
        self.child = child
        
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
        
def Merge(first,second):
    dummy = Node(-1)
    previous = dummy 
    while(first != None and second != None):
        if first.val <= second.val:
            previous.child = first 
            previous = first 
            first = first.child 
        else:
            previous.child = second 
            previous = second 
            second = second.child 
    while(first):
        previous.child = first 
        previous = first 
        first = first.child 
    while(second):
        previous.child = second 
        previous = second 
        second = second.child 
    return dummy.child 
    
def FlattenLL(head):
    if head is None or head.next is None:
        return head 
    next_head = FlattenLL(head.next)
    return Merge(head,next_head)

def display_child(head):
    curr = head 
    while(curr):
        print(curr)
        curr = curr.child
    
        
head = Node(5)
head.next = Node(10)
head.next.next = Node(19)
head.next.next.next = Node(28)

# Child list for 5
head.child = Node(7)
head.child.child = Node(8)
head.child.child.child = Node(30)

# Child list for 10
head.next.child = Node(20)

# Child list for 19
head.next.next.child = Node(22)
head.next.next.child.child = Node(50)

# Child list for 28
head.next.next.next.child = Node(35)
head.next.next.next.child.child = Node(40)
head.next.next.next.child.child.child = Node(45)

# Flatten and display
head = FlattenLL(head)
display_child(head)
