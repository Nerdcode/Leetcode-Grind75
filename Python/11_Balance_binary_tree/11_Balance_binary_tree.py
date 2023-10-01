# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def height(root):
            if root is None :
                return 0
            return max(height(root.left),height(root.right)) +1
        
        if root is None :
            return True
        left_height = height(root.left)
        right_height=height(root.right)

        if  abs(left_height-right_height)<=1 and self.isBalanced(root.left) is True and self.isBalanced(root.right) is True :
            return True 
        else :
            return False