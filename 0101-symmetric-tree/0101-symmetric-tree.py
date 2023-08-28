# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        stack = []

        stack.append([root.left,root.right])

        while stack:
            l, r = stack.pop()
            if l and r and l.val == r.val:
                stack.append([l.left,r.right])
                stack.append([l.right,r.left])
            else:
                if l is None and r is None:
                    continue
                else:
                    return False
        return True

        