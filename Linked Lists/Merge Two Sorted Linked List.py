"""
Docstring for Linked Lists.Merge Two Sorted Linked List

Time Complexity : O(n+m)
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
        
def Merge(head1,head2):
    dummy = Node(-1)
    previous = dummy 
    temp1 = head1
    temp2 = head2
    while(temp1 != None and temp2 != None):
        if temp1.val <= temp2.val:
            previous.next = temp1
            previous = temp1 
            temp1 = temp1.next 
        elif temp2.val < temp1.val:
            previous.next = temp2 
            previous = temp2 
            temp2 = temp2.next 
    while(temp1):
        previous.next = temp1 
        previous = temp1 
        temp1 = temp1.next 
    while(temp2):
        previous.next = temp2 
        previous = temp2 
        temp2 = temp2.next 
    return dummy.next  
        
L1 = [1,3,5,7,9]
L2 =[2,4,6,8,10]
head1 = None
for i in range(len(L1)):
    head1 = Insert(head1,L1[i])
head2 = None
for i in range(len(L2)):
    head2 = Insert(head2,L2[i])
head = Merge(head1,head2)
display(head)