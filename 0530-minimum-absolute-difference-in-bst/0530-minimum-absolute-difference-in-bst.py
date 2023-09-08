# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        mini = float('inf')
        prev = None

        def inorder(node):
            nonlocal mini, prev
            if node is None:
                return

            inorder(node.left)
            if prev is not None:
                mini = min(mini, abs(node.val - prev))
            prev = node.val
            inorder(node.right)
        
        inorder(root)
        return mini

