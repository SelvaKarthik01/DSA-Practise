""" 

Code


Testcase
Testcase
Test Result
101. Symmetric Tree
Solved
Easy
Topics
premium lock icon
Companies
Given the root of a binary tree, check whether it is a mirror of itself (i.e., symmetric around its center).

 

Example 1:


Input: root = [1,2,2,3,4,4,3]
Output: true
Example 2:


Input: root = [1,2,2,null,3,null,3]
Output: false
 

Constraints:

The number of nodes in the tree is in the range [1, 1000].
-100 <= Node.val <= 100
 

Follow up: Could you solve it both recursively and iteratively?
"""
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSymmetric(self, root):
        queue = []
        if root is None: 
            return False
        queue.append(root)
        while queue:
            levelsize = len(queue)
            currentlevel = []
            for i in range(levelsize):
                node = queue.pop(0)
                
                if node is not None:
                    queue.append(node.left)
                    queue.append(node.right)
                    currentlevel.append(node.val)
                else:
                    currentlevel.append(None)

               
            if len(currentlevel) == 1:
                continue
            mid = len(currentlevel)//2
            L = currentlevel[:mid]
            R = currentlevel[mid:]
            print(R)
            R.reverse()
            if L != R:
                print(L)
                print(R)
                return False
        return True

        """
        :type root: Optional[TreeNode]
        :rtype: bool
        """
        