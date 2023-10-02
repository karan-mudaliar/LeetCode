# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        res = []
        self.rev_inorder(root,res)

        return res[-1*k]
    

    def rev_inorder(self,node,res):
        if node:
            self.rev_inorder(node.right,res)
            # if k == 0:
            res.append(node.val)
            self.rev_inorder(node.left,res)

        