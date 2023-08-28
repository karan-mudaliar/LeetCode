# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        lefts, rights = float('-inf'),float('inf')
        return self.help(root,lefts,rights)

    def help(self,node,lval,rval):
        if not node:
            return True
        if node and (node.val >= rval or node.val <= lval):
            return False
                
        return self.help(node.left,lval,node.val) and                                self.help(node.right,node.val,rval)
            
