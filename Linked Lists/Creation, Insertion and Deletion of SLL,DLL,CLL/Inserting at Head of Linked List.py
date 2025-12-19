"""
Docstring for Linked Lists.Inserting at Head of Linked List

Time Complexity : O(1)
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
def Length(head):
    count = 0 
    curr = head 
    while(curr):
        curr = curr.next
        count += 1
    return count
def InsertatHead(head,val):
    newnode = Node(val)
    newnode.next = head 
    return newnode 
L = [1,2,3,4,5,6,7,8,9,10]
head = None
for i in range(len(L)):
    head = Insert(head,L[i])
val = int(input("Enter the Value to be Inserted : "))
head = InsertatHead(head,val)
display(head)