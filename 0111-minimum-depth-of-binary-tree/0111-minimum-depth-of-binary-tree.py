# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode],height = 0) -> int:
        if root is None:
            return height
        
        if root.left is None and root.right is None:
            return height + 1
        
        left = self.minDepth(root.left,height + 1) if root.left else float('inf')
        right = self.minDepth(root.right,height+ 1) if root.right else float('inf')

        return min(left,right)