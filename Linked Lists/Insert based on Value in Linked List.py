"""
Docstring for Linked Lists.Insert based on Value in Linked List

Insert it before the Value 

Time Complexity : O(n) or O(1)
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
def Insertatval(head,search,insert):
    newnode = Node(insert)
    if head.val == search:
        newnode.next = head 
        return newnode
    curr = head 
    while(curr.next.val != search):
        curr = curr.next 
    newnode.next = curr.next 
    curr.next = newnode 
    return head 
L = [1,2,3,4,5,6,7,8,9,10]
head = None
for i in range(len(L)):
    head = Insert(head,L[i])
search = int(input("Enter the Value to be Inserted before : "))
val = int(input("Enter the value to be Inserted : "))
head = Insertatval(head,search,val)
display(head)