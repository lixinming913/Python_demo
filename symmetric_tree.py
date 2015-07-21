# Symmetric Tree 
# Given a binary tree, check whether it is a mirror of itself (ie, symmetric around its center).

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param {TreeNode} root
    # @return {boolean}
    def isSymmetric(self, root):
        return self.isSymmetric_sub( root, root)
        
    def isSymmetric_sub(self, root1, root2):
        if root1 == None and root2 == None:
            return True
        
        if root1 == None or root2 == None:
            return False
            
        if (root1.val - root2.val) != 0:
            return False
            
        return self.isSymmetric_sub( root1.left, root2.right) and self.isSymmetric_sub(root1.right, root2.left)
        