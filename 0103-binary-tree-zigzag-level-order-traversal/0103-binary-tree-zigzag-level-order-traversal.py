# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        count = 0
        res = []
        if not root:
            return res
        arr = [root]

        while arr:
            next_level = []
            tmp = []
            for node in arr:
                if node:
                    tmp.append(node.val)
                if node and node.left:
                    next_level.append(node.left)
                if node and node.right:
                    next_level.append(node.right)
            if count % 2 == 1:
                res.append(tmp[::-1])
            else:
                res.append(tmp)
            # res.append(tmp)
            arr = next_level
            count += 1
        return res

                    


        