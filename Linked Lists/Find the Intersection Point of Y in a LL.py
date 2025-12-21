"""
Docstring for Linked Lists.Find the Intersection Point of Y in a LL

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

def Collision(head1,head2):
    temp1 = head1
    temp2 = head2 
    if head1 is None or head2 is None:
        return None 
    while(temp1 != temp2):
        temp1 = temp1.next 
        temp2 = temp2.next 
        if temp1 == temp2:
            return temp1 
        if temp1 is None:
            temp1 = head1 
        if temp2 is None:
            temp2 = head2 
    return temp1 

         
L = [1,2,3,4,5,6,7,8,9,10]
head = None
for i in range(len(L)):
    head = Insert(head,L[i])
if Collision(head,head):
    print(Collision(head,head))
else:
    print(None)
display(head)