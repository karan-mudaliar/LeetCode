# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrderBottom(self, root: Optional[TreeNode]) -> List[List[int]]:

        res = []
        if not root:
            return res
        
        arr = [root]

        while arr:
            next_level = []
            values = []

            for node in arr:
                if node:
                    values.append(node.val)
                if node and node.left:
                    next_level.append(node.left)
                if node and node.right:
                    next_level.append(node.right)
                
            res.append(values)
            arr = next_level
        return res[::-1]
        