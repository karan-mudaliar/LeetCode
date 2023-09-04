# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:

        return self.sums(root)

    
    def sums(self,root, count = 0):
        if root.left is None and root.right is None:
            return root.val + count * 10
        count = count * 10 + root.val
        left_sum = self.sums(root.left,count) if root.left is not None else 0
        right_sum = self.sums(root.right,count) if root.right is not None else 0
        
        return left_sum + right_sum
        
        