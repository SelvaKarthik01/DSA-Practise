"""
Docstring for Linked Lists.Add 1 to the Linked List


Another Apporach using Reversal yet Time Complexity might be High than the Recursive Solution

def Reverse(head):
    prev = None 
    curr = head 
    while(curr):
        future = curr.next 
        curr.next = prev 
        prev = curr 
        curr = future 
    return prev 

def Add_1(head):
    new_head = Reverse(head)
    carry = 1 
    curr = new_head
    prev = None
    while(curr != None):
        prev = curr
        sum = carry + curr.val 
        curr.val = sum % 10 
        carry = sum // 10 
        curr = curr.next 
    if carry:
        newnode = Node(carry)
        prev.next = newnode 
    head = Reverse(new_head)
    return head 
TC -> O(n) for Reversal + O(n) for Adding 1 + O(n) for Reversal to Original LL
SC -> O(1)
    
Time Complexity : O(n) for Adding 1 
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

def Add_1(head,carry):
    if head is None:
        return carry
    carry = Add_1(head.next,carry)
    sum = head.val + carry
    head.val = (sum)%10 
    carry = sum // 10 
    return carry
         
        
L = [9,9,9,9]
head = None
for i in range(len(L)):
    head = Insert(head,L[i])
carry = Add_1(head,1)
if carry == 1:
    newnode = Node(1)
    newnode.next = head 
    head = newnode 
display(head)