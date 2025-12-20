"""
Docstring for Linked Lists.Check if a LL is a Palindrome or Not

Another Solution with O(n) Space Complexity :

def isPalindrome(head):
    # write your code here
    stack = []
    curr = head 
    while(curr):
        stack.append(curr.data)
        curr = curr.next 
    curr= head 
    while(curr):
        if curr.data != stack.pop():
            return False 
        curr = curr.next
    return True 
    pass
    
TC -> O(n) + O(n)
SC -> O(n)

Time Complexity : O(n) for finding the Middle + O(n) for finding the Length + O(n//2) for Reversal + O(n//2) for Checking + O(n//2) for backtrack the changes done 
                  Total -> O(n) + O(n) + O(n//2) + O(n//2) + O(n//2) -> O(n)
                  
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

def Reverse(head):
    prev = None 
    curr = head 
    while(curr):
        future = curr.next 
        curr.next = prev 
        prev = curr 
        curr = future 
    return prev 
         
def findMiddle(head):
    fast = head 
    slow = head 
    while(fast is not None and fast.next is not None):
        fast = fast.next.next 
        slow = slow.next 
    return slow 

def LengthofLL(head):
    count = 0
    curr = head 
    while(curr):
        curr = curr.next 
        count += 1
    return count

def Palindrome_Check(head):
    middle = findMiddle(head)
    length = LengthofLL(head)
    if length % 2 == 0:
        second_head = middle 
    else:
        second_head = middle.next 
    second = Reverse(second_head)
    backtrack = second
    first = head 
    while(second != None):
        if first.val != second.val:
            Reverse(backtrack)
            return False
        first = first.next 
        second = second.next 
    Reverse(backtrack)   
    return True 
    
        
L = [1,2,3,2,1]
head = None
for i in range(len(L)):
    head = Insert(head,L[i])
print(Palindrome_Check(head))
display(head)
    