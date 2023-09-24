# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return
        
        arr = [root]
        res = []

        while arr:
            res.append(arr[-1].val)
            next_level = []
            for node in arr:
                if node and node.left:
                    next_level.append(node.left)
                if node and node.right:
                    next_level.append(node.right)
            
            arr = next_level
        return res
