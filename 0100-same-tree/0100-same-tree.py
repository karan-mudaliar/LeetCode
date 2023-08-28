# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:

        stack = []
        stack.append([p,q])

        while stack:
            l, r = stack.pop()
            if l and r and l.val == r.val:
                stack.append([l.right,r.right])
                stack.append([l.left,r.left])
        
            else:
                if l is None and r is None:
                    continue
                else: 
                    return False
        return True

