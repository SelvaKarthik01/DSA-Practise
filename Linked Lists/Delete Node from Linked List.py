"""
Docstring for Linked Lists.Delete Depending on Value from Linked List
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

def Delete(head,value):
    if head.val == value:
        return head.next 
    curr = head
    while(curr.val != value):
        curr = curr.next 
    curr.val = curr.next.val 
    curr.next = curr.next.next 
    return head 

L = [1,2,3,4,5,6,7,8,9,10]
head = None
for i in range(len(L)):
    head = Insert(head,L[i])
value = int(input("Enter the Value to be Deleted : "))
head = Delete(head,value)
display(head)