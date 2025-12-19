class Node:
    def __init__(self,val,next=None):
        self.val = val
        self.next = next
    def __str__(self):
        return f"{self.val}"
def CreateCLL(head,value):
    newnode = Node(value)
    if head is None:
        return newnode
    curr = head 
    while(curr.next != head):
        curr = curr.next 
    curr.next = newnode 
    newnode.next = head
        