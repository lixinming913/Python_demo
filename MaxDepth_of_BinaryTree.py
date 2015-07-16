/*
 *  Maximum Depth of Binary Tree
 *  Given a binary tree, find its maximum depth.
 */
 
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param {TreeNode} root
    # @return {integer}
    def maxDepth(self, root):
        if root == None :
            return 0
            
        if root.left == None and root.right == None:
            return 1
        
        left_depth = self.maxDepth(root.left)
        right_depth = self.maxDepth(root.right)
        
        if left_depth == 0:
            return right_depth + 1
        elif right_depth == 0:
            return left_depth + 1
        else:
            if left_depth < right_depth:
                return right_depth + 1
            else:
                return left_depth + 1
        