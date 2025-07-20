""" 
993. Cousins in Binary Tree
Solved
Easy
Topics
premium lock icon
Companies
Given the root of a binary tree with unique values and the values of two different nodes of the tree x and y, return true if the nodes corresponding to the values x and y in the tree are cousins, or false otherwise.

Two nodes of a binary tree are cousins if they have the same depth with different parents.

Note that in a binary tree, the root node is at the depth 0, and children of each depth k node are at the depth k + 1.

 

Example 1:


Input: root = [1,2,3,4], x = 4, y = 3
Output: false
Example 2:


Input: root = [1,2,3,null,4,null,5], x = 5, y = 4
Output: true
Example 3:


Input: root = [1,2,3,null,4], x = 2, y = 3
Output: false
 

Constraints:

The number of nodes in the tree is in the range [2, 100].
1 <= Node.val <= 100
Each node has a unique value.
x != y
x and y are exist in the tree.
"""
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isCousins(self, root, x, y):
        queue = []
        if root is None:
            return False
        queue.append(root)
        while queue:
            levelsize = len(queue)
            currentlevel = []
            for i in range(levelsize):
                node = queue.pop(0)
                if node.left and node.right:
                    if node.left.val == x and node.right.val == y:
                        return False
                    elif node.left.val == y and node.right.val == x:
                        return False

                if node.left is not None :
                        queue.append(node.left)
                if node.right is not None:
                        queue.append(node.right)
                currentlevel.append(node.val)
            if x in currentlevel:
                if y in currentlevel:
                    return True
                else:
                    return False
        

        """
        :type root: Optional[TreeNode]
        :type x: int
        :type y: int
        :rtype: bool
        """
        