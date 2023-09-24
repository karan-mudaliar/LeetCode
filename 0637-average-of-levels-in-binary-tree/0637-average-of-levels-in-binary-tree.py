# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        res = []

        if not root:
            return res
        arr = [root]
        

        while arr:
            tmp = []
            next_level = []

            for node in arr:
                if node:
                    tmp.append(node.val)
                if node and node.left:
                    next_level.append(node.left)
                if node and node.right:
                    next_level.append(node.right)
                
            res.append(sum(tmp)/len(tmp))
            arr = next_level
        return res
        

