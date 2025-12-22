"""
Docstring for Linked Lists.Design a Browser History

Time Complexity : O(1) for Visit + O(k) for forward + O(k) for back
                  Total -> O(n)
Space Complexity : O(1)

"""

class Node:
    def __init__(self,val,next=None,prev=None):
        self.val = val 
        self.next = next 
        self.prev = prev 
    def __str__(self):
        return f"{self.val}"

class BrowserHistory:
    def __init__(self,homepage):
        self.curr = Node(homepage)
    
    def visit(self,url):
        newnode = Node(url)
        newnode.prev = self.curr 
        self.curr.next = newnode 
        self.curr = newnode 
        return self.curr.val
    
    def back(self,steps):
        while(self.curr.prev != None and steps):
            self.curr = self.curr.prev 
            steps -= 1
        return self.curr.val 
    
    def forward(self,steps):
        while(self.curr.next != None and steps):
            self.curr = self.curr.next 
            steps -= 1
        return self.curr.val 

Browser = BrowserHistory("Google.com")
print(Browser.visit("Leetcode.com"))
print(Browser.visit("Instagram.com"))
print(Browser.visit("Facebook.com"))
print(Browser.back(1))
print(Browser.back(1))
print(Browser.forward(1))
print(Browser.visit("Leetcode.com"))
print(Browser.forward(2))
print(Browser.back(2))
print(Browser.back(7))

