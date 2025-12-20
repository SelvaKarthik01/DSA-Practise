"""
Docstring for Linked Lists.Add Two Numbers in a Linked List

2 -> 4-> 6      642
3 -> 8 -> 7     783
5-> 2->4->1     1425

Time Complexity : 
Space Complexity : 

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

def AddNumbers(head1,head2):
    carry = 0
    curr1 = head1 
    curr2 = head2
    dummy_node = Node(-1)
    curr = dummy_node 
    while(curr1 != None or curr2 != None):
        sum = carry 
        if curr1:
            sum += curr1.val 
        if curr2 :
            sum += curr2.val 
        newnode = Node(sum%10)
        carry = sum//10 
        curr.next = newnode 
        curr = curr.next 
        if curr1:
            curr1 = curr1.next 
        if curr2:
            curr2 = curr2.next 
    if carry != 0:
        newnode = Node(carry)
        curr.next = newnode 
    return dummy_node.next 

    
        
        
        
L1 = eval(input("Enter the Elements for L1: "))
L2 = eval(input("Enter the Elements for L2: "))
head1 = None
for i in range(len(L1)):
    head1 = Insert(head1,L1[i])
display(head1)
print()
head2 = None
for i in range(len(L2)):
    head2 = Insert(head2,L2[i])
display(head2)
print()
head = AddNumbers(head1,head2)
display(head)
