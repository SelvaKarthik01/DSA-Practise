"""
Docstring for Linked Lists.Delete the Tail of Linked List

Time Complexity : O(n) -> Travserse Till the End of the Linked List 
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
    if head == None :
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
def DeleteTail(head):
    if head == None or head.next == None:
        return None 
    curr = head 
    while(curr.next.next != None):
        curr = curr.next 
    curr.next = None 
    return head 
L = [1,2,3,4,5,6,7,8,9,10]
head = None
for i in range(len(L)):
    head = Insert(head,L[i])
head = DeleteTail(head)
display(head)



